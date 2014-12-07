    /*
     * To change this template, choose Tools | Templates
     * and open the template in the editor.
     */
    package util;

    import java.util.ArrayList;
    import java.util.Random;

    /**
     *
     * @author jDeRiggi
     */
    public class RandomIdMaker {

        private static Random r = new Random();
        private static char[] letters = new char[]{'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

        public static void main(String[] args) {
            ArrayList<String> list = new ArrayList<String>();
            int i = 0;
            while (i++ < 700) {
                String id = RandomIdMaker.getAlphaNumericNoOhZero(2);

                if (!list.contains(id)) {
                    list.add(id);
                    System.out.println(id);
                }else{
                    i = i-1;
                }


            }




        }
        public static String getAlphaNumericNoOhZero(int radius) {
            StringBuilder sb = new StringBuilder();
            int i = 0;
            while (i++ < radius) {
                sb.append(getDigitNoZero());
            }
            i = 0;
            while (i++ < radius) {
                sb.append(randomCharNoZero());
            }


            return sb.toString();
        }

        public static String getAlphaNumeric(int radius) {
            StringBuilder sb = new StringBuilder();
            int i = 0;
            while (i++ < radius) {
                sb.append(randomDigit());
            }
            i = 0;
            while (i++ < radius) {
                sb.append(randomChar());
            }


            return sb.toString();
        }

        public static String getNewSimId() {
            StringBuilder sb = new StringBuilder();
            int i = 0;
            while (i++ < 6) {
                if (Math.random() < 0.5f) {

                    sb.append(randomDigit());

                } else {

                    sb.append(randomChar());

                }
            }
            return sb.toString();
        }

        private static int randomDigit() {
            return r.nextInt(9);
        }
        private static int getDigitNoZero(){
            int rand = randomDigit();
            while(rand == 0){
                rand = randomDigit();
            }
            return rand;
        }
        
        private static char randomChar() {
            return letters[r.nextInt(25)];
        }
        
        private static char randomCharNoZero(){
            char noOh = randomChar();
            while(noOh == 'O'){
                noOh = randomChar();
            }
            return noOh;
        }
        
    }
