"""
       $('.btn_translation').click(function() {
        var snippet = $('.prefix > input').val();
        var output = '    "' + snippet + '": {' + "\n";
        output += '        "prefix": "' + snippet + '",' + "\n";
        output += '        "body": [' + "\n";
        var code = $('.code_before').val().replace(/\r\n|\r/g, "\n");
        var lines = code.split('\n');
        for(var i = 0; i < lines.length; i++) {
            var str = lines[i];
            str = str.replace(/\\/g, '\\\\');
            str = str.replace(/\"/g, '\\\"');
            str = str.replace(/\$/g, '\\\\$');
            str = '            \"' + str + '\",' + "\n";
            output = output + str;
        }
        output += '        ],' + "\n";
        output += '        "description": ""' + "\n";
        output += '    },' + "\n";
        $('.code_after').text(output);
    });

    """
import argparse


class Snippet:
    def __init__(self, prefix, code) -> None:
        self.prefix = prefix

        self.code = code

    def output(self):
        print(self.prefix)
        print(self.code)

    def output_json(self):
        print(self.prefix)
        print(self.code)


class FileLocation:
    def __init__(self, name, filename) -> None:
        self.name = name
        self.filename = filename


class System:
    def __init__(self) -> None:
        self.snippets = []

    def add_snippet(self, snippet: Snippet):
        self.snippets.append(snippet)

    def output(self):
        print("{")
        for snippet in self.snippets:
            snippet.output()
        print("}")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--headless', action='store_true',
                        help='whether or not headless')
    parser.add_argument('--driver', default=None, help='driver path')
    parser.add_argument('-i', '--input', help='input', type=int, required=True)

    parser.add_argument('-i', '--input', help='input', type=int, default=3)

    # リストを与えるとき nargsで指定した文字で分割 を使う
    parser.add_argument('--fruits', nargs='+',
                        help='list of fruits', required=True)
    # $ python ap.py --fruits apple banana orange
    # ['apple', 'banana', 'orange']

    # リストはappendでもできる。ただし、複数回指定する必要がある
    parser.add_argument('--fruits', action='append')
    # $ python ap.py --fruits apple --fruits banana --fruits orange
    # ['apple', 'banana', 'orange']

    # choice
    parser.add_argument(
        '--fruits', choices=['apple', 'banana', 'orange'], required=True)

    args = parser.parse_args()
    return args


def read_config_file(filename):
    pass


if __name__ == "__main__":
    args = parse_args()
    if args.f:
        filelocations = read_config_file()
    snippets = []
    for filelocation in filelocations:
        snippet = Snippet(filelocation.name, filelocation.filename)
        snippets.append(snippet)

    system = System()
    system.main()
