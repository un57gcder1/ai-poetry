RUN cd pytz-2020.1
RUN python setup.py install
RUN cd ..
RUN cd Django-1.11.29
RUN python setup.py install
RUN cd ..
RUN cd gunicorn-19.10.0
RUN python setup.py install
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "aipoetry.wsgi:application"]
