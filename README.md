# Zaza landing (prototype)

Static one-page shop for lifting slings. Orders are phone-only (no cart). Languages: Georgian (default), Russian, English.

## Local preview

JSON is loaded with `fetch`, so open the folder over HTTP:

```bash
npx serve
```

Then open the URL shown in the terminal (usually `http://localhost:3000`).

## Edit content

| What | File |
| --- | --- |
| Shop name, phone, email, address | [`data/site.json`](data/site.json) |
| UI strings (KA / RU / EN) | [`data/ui.json`](data/ui.json) |
| Products | [`data/products.json`](data/products.json) |
| Passport / document list | [`data/documents.json`](data/documents.json) |

### Add a product

1. Add an object to `data/products.json` (`id`, `category` = `textile` | `chain` | `rope`, `image`, `availability`, `priceFrom` or `null`, `name` in three languages).
2. Put the image under `images/` (SVG or JPG/PNG).

### Add a document

1. Drop a PDF into `documents/`.
2. Add an entry in `data/documents.json` with `file` and `title` in three languages.

## Netlify

- **Publish directory:** `.` (site root)
- **Build command:** leave empty

Or drag the whole project folder into Netlify Drop. `netlify.toml` already sets publish to `.`.
