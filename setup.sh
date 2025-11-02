mkdir -p ~/.streamlit/

echo "\
[server]\n\
headlessMode = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```