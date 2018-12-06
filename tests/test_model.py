from model.model import build_model


def test_handles_model(data):
    X_tr, X_te, y_tr, y_te = data
    build_model()
