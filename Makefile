IMAGES:=app nginx

images:
	for image in $(IMAGES); do \
		cd $$image; \
		docker build . -t exekias/beats-demo-$$image; \
		cd -; \
	done

push:
	for image in $(IMAGES); do \
		docker push exekias/beats-demo-$$image; \
	done
