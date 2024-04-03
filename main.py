#!/usr/bin/env python3

"""
Main cli or app entry point
"""
import yake
import click

# create a function that reads a file
def read_file(filename):
    with open(filename, encoding="utf-8") as myfile:
        return myfile.read()


# def extract keywords
def extract_keywords(text):
    kw_extractor = yake.KeywordExtractor()
    keywords = kw_extractor.extract_keywords(text)
    return keywords


# create a function that makes hash tags
def make_hashtags(keywords,tagslength=0):
    hashtags = []
    for keyword in keywords:
        hashtags.append("#" + keyword[0].replace(" ", ""))
    if tagslength:
        n =int(tagslength)
        return hashtags[:n]
    else:
        return hashtags

@click.group()
def cli():
    """A cli for keyword extraction"""


@cli.command("extract")
@click.argument("filename", default="text.txt")
def extract(filename):
    """Extract keywords from a file"""
    text = read_file(filename)
    keywords = extract_keywords(text)
    click.echo(keywords)


@cli.command("hashtags")
@click.argument("filename", default="text.txt")
@click.argument("tagslength", required=False)
def hashtagscli(filename,tagslength):
    """Extract keywords from a file and make hashtags"""
    text = read_file(filename)
    keywords = extract_keywords(text)
    hashtags = make_hashtags(keywords,tagslength)
    click.echo(hashtags)


if __name__ == "__main__":
    cli()
