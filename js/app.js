const LANG_KEY = "zaza-lang";
const SUPPORTED = ["ka", "ru", "en"];

const state = {
  lang: "ka",
  filter: "all",
  site: null,
  ui: null,
  products: [],
  documents: [],
};

function t(key) {
  return state.ui?.[state.lang]?.[key] ?? key;
}

function localized(map) {
  if (!map) return "";
  return map[state.lang] ?? map.ka ?? map.en ?? "";
}

async function loadData() {
  const [site, ui, products, documents] = await Promise.all([
    fetch("data/site.json").then((r) => r.json()),
    fetch("data/ui.json").then((r) => r.json()),
    fetch("data/products.json").then((r) => r.json()),
    fetch("data/documents.json").then((r) => r.json()),
  ]);

  state.site = site;
  state.ui = ui;
  state.products = products;
  state.documents = documents;
}

function setLanguage(lang) {
  if (!SUPPORTED.includes(lang)) lang = "ka";
  state.lang = lang;
  localStorage.setItem(LANG_KEY, lang);
  document.documentElement.lang = lang;
  document.title = `${state.site.name} — ${t("catalogTitle")}`;

  document.querySelectorAll(".lang-btn").forEach((btn) => {
    btn.classList.toggle("is-active", btn.dataset.lang === lang);
  });

  applyStaticCopy();
  renderProducts();
  renderDocuments();
}

function applyStaticCopy() {
  document.querySelectorAll("[data-i18n]").forEach((el) => {
    el.textContent = t(el.dataset.i18n);
  });

  document.querySelectorAll('[data-site="name"]').forEach((el) => {
    el.textContent = state.site.name;
  });
  document.querySelectorAll('[data-site="tagline"]').forEach((el) => {
    el.textContent = localized(state.site.tagline);
  });
  document.querySelectorAll('[data-site="phone"]').forEach((el) => {
    el.textContent = state.site.phone;
  });
  document.querySelectorAll('[data-site="phone-link"]').forEach((el) => {
    el.href = state.site.phoneHref;
  });
  document.querySelectorAll('[data-site="email"]').forEach((el) => {
    el.textContent = state.site.email;
  });
  document.querySelectorAll('[data-site="email-link"]').forEach((el) => {
    el.href = `mailto:${state.site.email}`;
  });
  document.querySelectorAll('[data-site="address"]').forEach((el) => {
    el.textContent = localized(state.site.address);
  });
}

function formatPrice(priceFrom) {
  if (priceFrom == null) return t("onRequest");
  return `${t("fromPrice")} ${priceFrom} ${t("currency")}`;
}

function renderProducts() {
  const grid = document.getElementById("product-grid");
  const status = document.querySelector("[data-status]");
  const items = state.products.filter(
    (p) => state.filter === "all" || p.category === state.filter
  );

  if (!items.length) {
    grid.innerHTML = `<p class="empty-state">${t("emptyFilter")}</p>`;
    status.hidden = true;
    return;
  }

  status.hidden = true;
  grid.innerHTML = items
    .map((product) => {
      const availabilityLabel =
        product.availability === "in_stock" ? t("inStock") : t("onOrder");
      const availabilityClass =
        product.availability === "in_stock" ? "" : "is-order";

      return `
        <article class="product-card">
          <div class="product-media">
            <img src="${product.image}" alt="" loading="lazy" width="160" height="160" />
          </div>
          <div class="product-body">
            <h3>${localized(product.name)}</h3>
            <p class="availability ${availabilityClass}">${availabilityLabel}</p>
            <p class="price">${formatPrice(product.priceFrom)}</p>
            <a class="btn btn-ghost" href="${state.site.phoneHref}">${t("callToOrder")}</a>
          </div>
        </article>
      `;
    })
    .join("");
}

function renderDocuments() {
  const list = document.getElementById("document-list");
  list.innerHTML = state.documents
    .map(
      (doc) => `
      <li class="document-item">
        <a class="document-link" href="${doc.file}" download>
          <span class="pdf-icon" aria-hidden="true">PDF</span>
          <span class="document-title">${localized(doc.title)}</span>
          <span class="document-action">${t("download")}</span>
        </a>
      </li>
    `
    )
    .join("");
}

function bindEvents() {
  document.querySelectorAll(".lang-btn").forEach((btn) => {
    btn.addEventListener("click", () => setLanguage(btn.dataset.lang));
  });

  document.querySelectorAll(".filter-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      state.filter = btn.dataset.filter;
      document.querySelectorAll(".filter-btn").forEach((el) => {
        el.classList.toggle("is-active", el === btn);
      });
      renderProducts();
    });
  });
}

async function init() {
  const saved = localStorage.getItem(LANG_KEY);
  state.lang = SUPPORTED.includes(saved) ? saved : "ka";

  try {
    await loadData();
  } catch (error) {
    document.getElementById("product-grid").innerHTML =
      "<p class=\"empty-state\">Failed to load catalog. Serve the folder over HTTP (e.g. npx serve).</p>";
    console.error(error);
    return;
  }

  bindEvents();
  setLanguage(state.lang);
}

init();
