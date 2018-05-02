import records

def main():
    engine = records.Database('sqlite:///./xkcd.db')
    engine.query('DROP TABLE IF EXISTS xkcd_words')
    engine.query('CREATE TABLE xkcd_words (xkcd_word_id integer, word varchar(255),PRIMARY KEY (xkcd_word_id))')
    with open('words_alpha.txt') as f:
        for line in f:
            query ="INSERT INTO xkcd_words (word) VALUES (:line)"
            engine.query(query,False,line=line)
    engine.close()



if __name__ == '__main__':
    main()