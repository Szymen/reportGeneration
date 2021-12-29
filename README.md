# Raport Generator << Creative Name soon>>

With this project you can quickly render personalised raports for every answer you got in csv file. So f.e. when writing down comments for each assessment you can then easily provide feedback for someone you checked.

## Getting Started

### Prerequisites
In order to use the raport generator you have to either have:

* Docker installed
* PIP for Python 3.9.9

### Installing/Building

PIP instalation variant
```
pip3 install -r requirements.txt
```

Docker preparation variant

```
docker build --progress=plain . -t report_generator
```


## Running the tests

all in test_getNumberFromFieldValue.py

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Usage

Put CSV files into data folder

```mermaid
docker run -it -v ${PWD}:/app --rm report_generator csv_file_name.csv
```

## Built With

* [Stack overflow ](https://stackoverflow.com/) - You know why

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use no versions at all for now.

## Authors

* **Szymon Maslowski** - *Programming work* - [Szymen](https://github.com/Szymen)
* **Aleks Fuchs** - *Vision and usability consultant*

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
