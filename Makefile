DC = docker-compose
EXEC = docker exec -it
LOGS = docker logs
APP = ./docker-compose.yml
APP_SERVICE = mr-robot-app

PROTOS_PATH =./app/infra/grpc/protos

# PROTOS_SRC = $(wildcard $(PROTOS_PATH)/*.proto)
# PROTOS_PY = $(patsubst $(PROTOS_PATH)/%.proto, $(PROTOS_PATH)/%_pb2.py, $(PROTO_SRC))
# PROTOS_GRPC_PY = $(patsubst $(PROTOS_PATH)/%.proto, $(PROTOS_PATH)/%_pb2_grpc.py, $(PROTO_SRC))
# PROTOS_PYI = $(patsubst $(PROTOS_PATH)/%.proto, $(PROTOS_PATH)/%_pb2.pyi, $(PROTO_SRC))

# ------------------------------------------

# PROTOS_OUT = $(PROTOS_PY) $(PROTOS_GRPC_PY) $(PROTOS_PYI)

# $(PROTOS_PATH)/%_pb2.py $(PROTOS_PATH)/%_pb2_grpc.py $(PROTOS_PATH)/%_pb2.pyi: $(PROTOS_PATH)/%.proto
#     python -m grpc_tools.protoc -I./$(PROTOS_PATH) --python_out=./$(PROTOS_PATH) --grpc_python_out=./$(PROTOS_PATH) --mypy_out=./$(PROTOS_PATH) $<

.PHONY: app
app:
	${DC} -f ${APP} up --build -d

.PHONY: app-down
app-down:
	${DC} -f ${APP} down

.PHONY: app-logs
app-logs:
	${DC} -f ${APP} logs -f ${APP_SERVICE}


.PHONY: proto
proto:
	python -m grpc_tools.protoc --proto_path=$(PROTOS_PATH) --python_out=$(PROTOS_PATH) --pyi_out=$(PROTOS_PATH) --grpc_python_out=$(PROTOS_PATH) $(PROTOS_PATH)/test.proto


# ------------------------------------------