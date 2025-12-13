import { defineConfig } from "vite";

export default defineConfig({
  build: {
    rollupOptions: {
      input: [
        "web/scripts/app.js",
        "web/styles/app.scss",
      ],
    },
    outDir: "app/static/bundle",
    // map from original path to compiled file path
    manifest: "manifest.json",
    // (optional)
    minify: false,
  },
  plugins: [
    // since our template html is not handled by vite at all, we would like to
    // tell vite in some way that we want reload feature. solution copied from:
    // https://stackoverflow.com/questions/77461040/can-i-get-vite-to-reload-the-browser-on-every-html-change
    {
      name: "reload",
      configureServer(server) {
        const { ws, watcher } = server;
        watcher.on("change", (file) => {
          if (file.endsWith(".jinja.html")) {
            ws.send({
              type: "full-reload",
            });
          }
        });
      }
    }
  ]
});
