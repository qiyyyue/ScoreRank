<?php
/**
 * Created by PhpStorm.
 * User: qiyyy
 * Date: 2018/10/16
 * Time: 15:08
 */

class curl_post
{
    public static function post($url, $post_data = '', $timeout = 10){

        $ch = curl_init();

        curl_setopt ($ch, CURLOPT_URL, $url);

        curl_setopt($ch, CURLOPT_POSTFIELDS, $post_data);

        curl_setopt($ch,CURLOPT_SSL_VERIFYPEER, false);

        curl_setopt ($ch, CURLOPT_RETURNTRANSFER, 1);

        curl_setopt ($ch, CURLOPT_CONNECTTIMEOUT, $timeout);

        curl_setopt ($ch, CURLOPT_CUSTOMREQUEST, 'POST');

        $file_contents = curl_exec($ch);

        curl_close($ch);

        return $file_contents;
    }
}