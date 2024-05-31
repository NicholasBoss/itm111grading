-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
-- ~
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
-- ~
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
-- ~

-- -----------------------------------------------------
-- Schema film
-- -----------------------------------------------------
-- ~
DROP SCHEMA IF EXISTS `film` ;
-- ~

-- -----------------------------------------------------
-- Schema film
-- -----------------------------------------------------
-- ~
CREATE SCHEMA IF NOT EXISTS `film` ;
-- ~
-- ~
USE `film` ;
-- ~

-- -----------------------------------------------------
-- Table `film`.`rating`
-- -----------------------------------------------------
-- ~
DROP TABLE IF EXISTS `film`.`rating` ;
-- ~

-- ~
CREATE TABLE IF NOT EXISTS `film`.`rating` (
  `rating_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `rating_level` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`rating_id`))
ENGINE = InnoDB;
-- ~


-- -----------------------------------------------------
-- Table `film`.`movie`
-- -----------------------------------------------------
-- ~
DROP TABLE IF EXISTS `film`.`movie` ;
-- ~

-- ~
CREATE TABLE IF NOT EXISTS `film`.`movie` (
  `movie_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `movie_title` VARCHAR(45) NOT NULL,
  `movie_year` INT NOT NULL,
  `rating_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`movie_id`),
  INDEX `fk_movie_rating1_idx` (`rating_id` ASC) VISIBLE,
  CONSTRAINT `fk_movie_rating1`
    FOREIGN KEY (`rating_id`)
    REFERENCES `film`.`rating` (`rating_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
-- ~


-- -----------------------------------------------------
-- Table `film`.`actor`
-- -----------------------------------------------------
-- ~
DROP TABLE IF EXISTS `film`.`actor` ;
-- ~

-- ~
CREATE TABLE IF NOT EXISTS `film`.`actor` (
  `actor_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `actor_fname` VARCHAR(45) NOT NULL,
  `actor_lname` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`actor_id`))
ENGINE = InnoDB;
-- ~


-- -----------------------------------------------------
-- Table `film`.`price`
-- -----------------------------------------------------
-- ~
DROP TABLE IF EXISTS `film`.`price` ;
-- ~

-- ~
CREATE TABLE IF NOT EXISTS `film`.`price` (
  `price_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `price_value` DECIMAL(4,2) NOT NULL,
  PRIMARY KEY (`price_id`))
ENGINE = InnoDB;
-- ~


-- -----------------------------------------------------
-- Table `film`.`media`
-- -----------------------------------------------------
-- ~
DROP TABLE IF EXISTS `film`.`media` ;
-- ~

-- ~
CREATE TABLE IF NOT EXISTS `film`.`media` (
  `media_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `media_type` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`media_id`))
ENGINE = InnoDB;
-- ~


-- -----------------------------------------------------
-- Table `film`.`feature`
-- -----------------------------------------------------
-- ~
DROP TABLE IF EXISTS `film`.`feature` ;
-- ~

-- ~
CREATE TABLE IF NOT EXISTS `film`.`feature` (
  `feature_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `feature_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`feature_id`))
ENGINE = InnoDB;
-- ~


-- -----------------------------------------------------
-- Table `film`.`genre`
-- -----------------------------------------------------
-- ~
DROP TABLE IF EXISTS `film`.`genre` ;
-- ~

-- ~
CREATE TABLE IF NOT EXISTS `film`.`genre` (
  `genre_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `genre_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`genre_id`))
ENGINE = InnoDB;
-- ~


-- -----------------------------------------------------
-- Table `film`.`studio`
-- -----------------------------------------------------
-- ~
DROP TABLE IF EXISTS `film`.`studio` ;
-- ~

-- ~
CREATE TABLE IF NOT EXISTS `film`.`studio` (
  `studio_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `studio_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`studio_id`))
ENGINE = InnoDB;
-- ~


-- -----------------------------------------------------
-- Table `film`.`cast`
-- -----------------------------------------------------
-- ~
DROP TABLE IF EXISTS `film`.`cast` ;
-- ~

-- ~
CREATE TABLE IF NOT EXISTS `film`.`cast` (
  `cast_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `movie_id` INT UNSIGNED NOT NULL,
  `actor_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`cast_id`),
  INDEX `fk_cast_movie_idx` (`movie_id` ASC) VISIBLE,
  INDEX `fk_cast_actor1_idx` (`actor_id` ASC) VISIBLE,
  CONSTRAINT `fk_cast_movie`
    FOREIGN KEY (`movie_id`)
    REFERENCES `film`.`movie` (`movie_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cast_actor1`
    FOREIGN KEY (`actor_id`)
    REFERENCES `film`.`actor` (`actor_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
-- ~


-- -----------------------------------------------------
-- Table `film`.`movie_studio`
-- -----------------------------------------------------
-- ~
DROP TABLE IF EXISTS `film`.`movie_studio` ;
-- ~

-- ~
CREATE TABLE IF NOT EXISTS `film`.`movie_studio` (
  `movie_studio_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `movie_id` INT UNSIGNED NOT NULL,
  `studio_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`movie_studio_id`),
  INDEX `fk_movie_studio_movie1_idx` (`movie_id` ASC) VISIBLE,
  INDEX `fk_movie_studio_studio1_idx` (`studio_id` ASC) VISIBLE,
  CONSTRAINT `fk_movie_studio_movie1`
    FOREIGN KEY (`movie_id`)
    REFERENCES `film`.`movie` (`movie_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_movie_studio_studio1`
    FOREIGN KEY (`studio_id`)
    REFERENCES `film`.`studio` (`studio_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
-- ~


-- -----------------------------------------------------
-- Table `film`.`movie_genre`
-- -----------------------------------------------------
-- ~
DROP TABLE IF EXISTS `film`.`movie_genre` ;
-- ~

-- ~
CREATE TABLE IF NOT EXISTS `film`.`movie_genre` (
  `movie_genre_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `movie_id` INT UNSIGNED NOT NULL,
  `genre_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`movie_genre_id`),
  INDEX `fk_movie_genre_movie1_idx` (`movie_id` ASC) VISIBLE,
  INDEX `fk_movie_genre_genre1_idx` (`genre_id` ASC) VISIBLE,
  CONSTRAINT `fk_movie_genre_movie1`
    FOREIGN KEY (`movie_id`)
    REFERENCES `film`.`movie` (`movie_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_movie_genre_genre1`
    FOREIGN KEY (`genre_id`)
    REFERENCES `film`.`genre` (`genre_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
-- ~


-- -----------------------------------------------------
-- Table `film`.`movie_feature`
-- -----------------------------------------------------
-- ~
DROP TABLE IF EXISTS `film`.`movie_feature` ;
-- ~

-- ~
CREATE TABLE IF NOT EXISTS `film`.`movie_feature` (
  `movie_feature_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `movie_id` INT UNSIGNED NOT NULL,
  `feature_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`movie_feature_id`),
  INDEX `fk_movie_feature_movie1_idx` (`movie_id` ASC) VISIBLE,
  INDEX `fk_movie_feature_feature1_idx` (`feature_id` ASC) VISIBLE,
  CONSTRAINT `fk_movie_feature_movie1`
    FOREIGN KEY (`movie_id`)
    REFERENCES `film`.`movie` (`movie_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_movie_feature_feature1`
    FOREIGN KEY (`feature_id`)
    REFERENCES `film`.`feature` (`feature_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
-- ~


-- -----------------------------------------------------
-- Table `film`.`movie_media`
-- -----------------------------------------------------
-- ~
DROP TABLE IF EXISTS `film`.`movie_media` ;
-- ~

-- ~
CREATE TABLE IF NOT EXISTS `film`.`movie_media` (
  `movie_media_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `movie_id` INT UNSIGNED NOT NULL,
  `media_id` INT UNSIGNED NOT NULL,
  `price_id` INT UNSIGNED NULL,
  PRIMARY KEY (`movie_media_id`),
  INDEX `fk_movie_media_movie1_idx` (`movie_id` ASC) VISIBLE,
  INDEX `fk_movie_media_media1_idx` (`media_id` ASC) VISIBLE,
  INDEX `fk_movie_media_price1_idx` (`price_id` ASC) VISIBLE,
  CONSTRAINT `fk_movie_media_movie1`
    FOREIGN KEY (`movie_id`)
    REFERENCES `film`.`movie` (`movie_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_movie_media_media1`
    FOREIGN KEY (`media_id`)
    REFERENCES `film`.`media` (`media_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_movie_media_price1`
    FOREIGN KEY (`price_id`)
    REFERENCES `film`.`price` (`price_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
-- ~


SET SQL_MODE=@OLD_SQL_MODE;
-- ~
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
-- ~
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
-- ~

-- ~
USE film;
-- ~

-- ~
INSERT INTO rating
(rating_level)
VALUES
('G')
, ('PG')
, ('PG-13');
-- ~

-- ~
INSERT INTO movie
( movie_title
, movie_year
, rating_id )
VALUES
( 'Toy Story'
, 1995
, (SELECT rating_id FROM rating WHERE rating_level = 'G')
),
( 'Toy Story 2'
, 1999
, (SELECT rating_id FROM rating WHERE rating_level = 'G')
),
( 'Brigadoone'
, 1954
, (SELECT rating_id FROM rating WHERE rating_level = 'G')
),
( 'The Empire Strikes Back'
, 1980
, (SELECT rating_id FROM rating WHERE rating_level = 'PG')
),
( 'Coda'
, 2021
, (SELECT rating_id FROM rating WHERE rating_level = 'PG-13')
),
( 'Black Panther: Wakanda Forever'
, 2022
, (SELECT rating_id FROM rating WHERE rating_level = 'PG-13')
);
-- ~

-- ~
INSERT INTO genre
(genre_name)
VALUES
('Family')
, ('Animated')
, ('Musical')
, ('Romance')
, ('Sci-Fi')
, ('Comedy')
, ('Drama')
, ('Music')
, ('Action')
, ('Adventure')
, ('Thriller')
, ('Fantasy');
-- ~

-- ~
INSERT INTO feature
(feature_name)
VALUES
('Bloopers')
, ('Actor Interviews')
, ('Cut Scenes')
, ('Trailers');
-- ~

-- ~
INSERT INTO studio
(studio_name)
VALUES
('Pixar')
, ('MGM')
, ('20th Century Fox')
, ('Apple TV+')
, ('Marvel')
, ('Disney');
-- ~

-- ~
INSERT INTO actor
(actor_fname, actor_lname)
VALUES
('Tom', 'Hanks')
, ('Tim','Allen')
, ('Annie','Potts')
, ('John','Ratzenberger')
, ('Gene','Kelly')
, ('Cyd','Charisse')
, ('Van','Johnson')
, ('Harrison','Ford')
, ('Carrie','Fisher')
, ('Mark','Hamill')
, ('Emilia','Jones')
, ('Marlee','Matlin')
, ('Troy','Kotsur')
, ('Letitia','Wright')
, ('Angela','Bassett')
, ('Danai','Gurira')
, ('Lupita','Nyong''o');
-- ~

-- ~
INSERT INTO price
(price_value)
VALUES
(19.95)
, (24.95)
, (35.00)
, (19.99);
-- ~

-- ~
INSERT INTO media
(media_type)
VALUES
('DVD')
, ('Blu-Ray')
, ('Streaming')
, ('HD');
-- ~

-- ~
INSERT INTO cast
( movie_id
, actor_id )
VALUES
( (SELECT movie_id FROM movie WHERE movie_title = 'Toy Story')
, (SELECT actor_id FROM actor WHERE actor_fname = 'Tom')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Toy Story')
, (SELECT actor_id FROM actor WHERE actor_fname = 'Tim')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Toy Story')
, (SELECT actor_id FROM actor WHERE actor_fname = 'Annie')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Toy Story')
, (SELECT actor_id FROM actor WHERE actor_fname = 'John')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Toy Story 2')
, (SELECT actor_id FROM actor WHERE actor_fname = 'Tom')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Toy Story 2')
, (SELECT actor_id FROM actor WHERE actor_fname = 'Tim')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Toy Story 2')
, (SELECT actor_id FROM actor WHERE actor_fname = 'Annie')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Toy Story 2')
, (SELECT actor_id FROM actor WHERE actor_fname = 'John')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Brigadoone')
, (SELECT actor_id FROM actor WHERE actor_fname = 'Gene')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Brigadoone')
, (SELECT actor_id FROM actor WHERE actor_fname = 'Cyd')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Brigadoone')
, (SELECT actor_id FROM actor WHERE actor_fname = 'Van')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'The Empire Strikes Back')
, (SELECT actor_id FROM actor WHERE actor_fname = 'Harrison')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'The Empire Strikes Back')
, (SELECT actor_id FROM actor WHERE actor_fname = 'Carrie')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'The Empire Strikes Back')
, (SELECT actor_id FROM actor WHERE actor_fname = 'Mark')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Coda')
, (SELECT actor_id FROM actor WHERE actor_fname = 'Emilia')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Coda')
, (SELECT actor_id FROM actor WHERE actor_fname = 'Marlee')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Coda')
, (SELECT actor_id FROM actor WHERE actor_fname = 'Troy')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Black Panther: Wakanda Forever')
, (SELECT actor_id FROM actor WHERE actor_fname = 'Letitia')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Black Panther: Wakanda Forever')
, (SELECT actor_id FROM actor WHERE actor_fname = 'Angela')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Black Panther: Wakanda Forever')
, (SELECT actor_id FROM actor WHERE actor_fname = 'Danai')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Black Panther: Wakanda Forever')
, (SELECT actor_id FROM actor WHERE actor_fname = 'Lupita')
);
-- ~

-- ~
INSERT INTO movie_genre
( movie_id
, genre_id )
VALUES
( (SELECT movie_id FROM movie WHERE movie_title = 'Toy Story')
, (SELECT genre_id FROM genre WHERE genre_name = 'Family')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Toy Story')
, (SELECT genre_id FROM genre WHERE genre_name = 'Animated')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Toy Story 2')
, (SELECT genre_id FROM genre WHERE genre_name = 'Family')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Toy Story 2')
, (SELECT genre_id FROM genre WHERE genre_name = 'Animated')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Brigadoone')
, (SELECT genre_id FROM genre WHERE genre_name = 'Musical')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Brigadoone')
, (SELECT genre_id FROM genre WHERE genre_name = 'Romance')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'The Empire Strikes Back')
, (SELECT genre_id FROM genre WHERE genre_name = 'Sci-Fi')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Coda')
, (SELECT genre_id FROM genre WHERE genre_name = 'Comedy')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Coda')
, (SELECT genre_id FROM genre WHERE genre_name = 'Drama')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Coda')
, (SELECT genre_id FROM genre WHERE genre_name = 'Music')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Black Panther: Wakanda Forever')
, (SELECT genre_id FROM genre WHERE genre_name = 'Action')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Black Panther: Wakanda Forever')
, (SELECT genre_id FROM genre WHERE genre_name = 'Adventure')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Black Panther: Wakanda Forever')
, (SELECT genre_id FROM genre WHERE genre_name = 'Drama')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Black Panther: Wakanda Forever')
, (SELECT genre_id FROM genre WHERE genre_name = 'Thriller')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Black Panther: Wakanda Forever')
, (SELECT genre_id FROM genre WHERE genre_name = 'Fantasy')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Black Panther: Wakanda Forever')
, (SELECT genre_id FROM genre WHERE genre_name = 'Sci-Fi')
);
-- ~

-- ~
INSERT INTO movie_feature
( movie_id
, feature_id )
VALUES
( (SELECT movie_id FROM movie WHERE movie_title = 'Toy Story')
, (SELECT feature_id FROM feature WHERE feature_name = 'Bloopers')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Toy Story 2')
, (SELECT feature_id FROM feature WHERE feature_name = 'Actor Interviews')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'The Empire Strikes Back')
, (SELECT feature_id FROM feature WHERE feature_name = 'Cut Scenes')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'The Empire Strikes Back')
, (SELECT feature_id FROM feature WHERE feature_name = 'Bloopers')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Coda')
, (SELECT feature_id FROM feature WHERE feature_name = 'Trailers')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Black Panther: Wakanda Forever')
, (SELECT feature_id FROM feature WHERE feature_name = 'Trailers')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Black Panther: Wakanda Forever')
, (SELECT feature_id FROM feature WHERE feature_name = 'Bloopers')
);
-- ~

-- ~
INSERT INTO movie_studio
( movie_id
, studio_id )
VALUES
( (SELECT movie_id FROM movie WHERE movie_title = 'Toy Story')
, (SELECT studio_id FROM studio WHERE studio_name = 'Pixar')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Toy Story 2')
, (SELECT studio_id FROM studio WHERE studio_name = 'Pixar')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Brigadoone')
, (SELECT studio_id FROM studio WHERE studio_name = '20th Century Fox')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Coda')
, (SELECT studio_id FROM studio WHERE studio_name = 'Apple TV+')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Black Panther: Wakanda Forever')
, (SELECT studio_id FROM studio WHERE studio_name = 'Marvel')
),
( (SELECT movie_id FROM movie WHERE movie_title = 'Black Panther: Wakanda Forever')
, (SELECT studio_id FROM studio WHERE studio_name = 'Disney')
);
-- ~

-- ~
INSERT INTO movie_media
( movie_id
, media_id
, price_id )
VALUES
( (SELECT movie_id FROM movie WHERE movie_title = 'Toy Story')
, (SELECT media_id FROM media WHERE media_type = 'DVD')
, (SELECT price_id FROM price WHERE price_value = 19.95)
), 
( (SELECT movie_id FROM movie WHERE movie_title = 'Toy Story 2')
, (SELECT media_id FROM media WHERE media_type = 'DVD')
, (SELECT price_id FROM price WHERE price_value = 24.95)
), 
( (SELECT movie_id FROM movie WHERE movie_title = 'Brigadoone')
, (SELECT media_id FROM media WHERE media_type = 'DVD')
, (SELECT price_id FROM price WHERE price_value = 19.95)
), 
( (SELECT movie_id FROM movie WHERE movie_title = 'The Empire Strikes Back')
, (SELECT media_id FROM media WHERE media_type = 'Blu-Ray')
, (SELECT price_id FROM price WHERE price_value = 35.00)
), 
( (SELECT movie_id FROM movie WHERE movie_title = 'Coda')
, (SELECT media_id FROM media WHERE media_type = 'Streaming')
, NULL
), 
( (SELECT movie_id FROM movie WHERE movie_title = 'Black Panther: Wakanda Forever')
, (SELECT media_id FROM media WHERE media_type = 'Streaming')
, NULL
), 
( (SELECT movie_id FROM movie WHERE movie_title = 'Black Panther: Wakanda Forever')
, (SELECT media_id FROM media WHERE media_type = 'Streaming')
, (SELECT price_id FROM price WHERE price_value = 19.99)
);
-- ~
