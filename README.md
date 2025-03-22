# Movie Language Model
> This project first scrapes movie scripts from the web and then uses that data in training for a language model which creates movies.
This repo uses the Base Llama-3.2-1B Model and fine tunes the model to the movie scripts that have been scraped.

## Installation

```sh
pip install -r requirements.txt
python3 ./movie_scraper/scraper.py
```

## Usage example

A few motivating and useful examples of how your product can be used. Spice this up with code blocks and potentially more screenshots.


## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

```sh
make install
npm test
```

start-notebook.py --NotebookApp.token='my-token'

## Meta

David Wehrlin – djwehrlin@gmail.com

Distributed under the MIT License. See ``LICENSE`` for more information.

[https://davidwehrlin.github.io/](https://davidwehrlin.github.io/)

## Contributing

1. Fork it (<https://github.com/davidwehrlin/movie-language-model/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request




|===========================================================================|\n|                  PyTorch CUDA memory summary, device ID 0                 |\n|---------------------------------------------------------------------------|\n|            CUDA OOMs: 2            |        cudaMalloc retries: 2         |\n|===========================================================================|\n|        Metric         | Cur Usage  | Peak Usage | Tot Alloc  | Tot Freed  |\n|---------------------------------------------------------------------------|\n| Allocated memory      |  25828 MiB |  25828 MiB |  25828 MiB |      0 B   |\n|---------------------------------------------------------------------------|\n| Active memory         |  25828 MiB |  25828 MiB |  25828 MiB |      0 B   |\n|---------------------------------------------------------------------------|\n| Requested memory      |  25756 MiB |  25756 MiB |  25756 MiB |      0 B   |\n|---------------------------------------------------------------------------|\n| GPU reserved memory   |  30662 MiB |  30662 MiB |  30662 MiB |      0 B   |\n|---------------------------------------------------------------------------|\n| Non-releasable memory |   4833 MiB |   4844 MiB |  20535 MiB |  15702 MiB |\n|---------------------------------------------------------------------------|\n| Allocations           |    4499    |    4499    |    4499    |       0    |\n|---------------------------------------------------------------------------|\n| Active allocs         |    4499    |    4499    |    4499    |       0    |\n|---------------------------------------------------------------------------|\n| GPU reserved segments |    1542    |    1542    |    1542    |       0    |\n|---------------------------------------------------------------------------|\n| Non-releasable allocs |    1394    |    1394    |    1423    |      29    |\n|---------------------------------------------------------------------------|\n| Oversize allocations  |       0    |       0    |       0    |       0    |\n|---------------------------------------------------------------------------|\n| Oversize GPU segments |       0    |       0    |       0    |       0    |\n|===========================================================================|\n