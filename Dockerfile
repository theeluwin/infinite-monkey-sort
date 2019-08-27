# ubuntu
FROM frolvlad/alpine-python3
LABEL maintainer="Jamie Seol <theeluwin@gmail.com>"

# init
RUN mkdir -p /workspace
WORKDIR /workspace

# install packages
RUN pip3 install nose nose-exclude flake8 coverage

# run
ADD . /workspace/
ENTRYPOINT []
CMD ["nosetests", "--config=.noserc"]
