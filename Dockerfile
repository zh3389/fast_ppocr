FROM hdgigante/python-opencv:4.7.0-debian
RUN pip3 install python-multipart rapidocr_api -i https://pypi.tuna.tsinghua.edu.cn/simple --break-system-packages && pip3 cache purge

EXPOSE 9001

CMD ["rapidocr_api", "-ip", "0.0.0.0", "-p", "9001"]
