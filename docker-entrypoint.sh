#!/bin/bash
umap migrate
gunicorn umap.wsgi