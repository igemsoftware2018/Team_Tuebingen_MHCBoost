import logging

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
LOG = logging.getLogger("test_src")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)


def read_training_data():
    LOG.info("Reading in training data")
    with open("data/training_data/iedb_A*01:01_9_only.txt", 'r') as f:
        read_data = f.read()
        print(read_data)
    LOG.info("Successfully read in training data")

