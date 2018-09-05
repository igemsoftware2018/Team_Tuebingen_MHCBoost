import logging

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("test_src")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def some_function():
    LOG.info("Running some_function")
    print("whatsup")
    LOG.info("Successfully run some_function")

    with open("data/some_data.txt", 'r') as f:
        read_data = f.read()
        print(read_data)
