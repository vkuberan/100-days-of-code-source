<?php


class Singleton
{
    private static $instance;

    private function __construct()
    {
    }
    private function __clone()
    {
    }
    private function __wakeup()
    {
    }

    public static function getInstance()
    {
        if (null === self::$instance) {
            self::$instance = new self();
            echo "Created the Singleton Object for the first time. \n";
        } else {
            echo "Returning the already created Singleton object. \n";
        }
        return self::$instance;
    }
}

// This will trigger an error
// $s1 = new Singleton();

$s1 = Singleton::getInstance();
$s2 = Singleton::getInstance();
