function naturalSort(a, b) {
              var NUMBER_GROUPS = /(-?\d*\.?\d+)/g;
            var aa = String(a).split(NUMBER_GROUPS),
                bb = String(b).split(NUMBER_GROUPS),
                min = Math.min(aa.length, bb.length);

            for (var i = 0; i < min; i++) {
                var x = parseFloat(aa[i]) || aa[i].toLowerCase(),
                    y = parseFloat(bb[i]) || bb[i].toLowerCase();
                if (x < y) return -1;
                else if (x > y) return 1;
            }

            return 0;
        }
        
// arr1=[1,2,4,5,75,3,4,56,7,8];

// arr2=["cat","mat", "rat", "snap", "test", "foo", "bar", "foobar"];

// arr3=["01/01/2014", "02/01/2014", "04/03/1991", "04/08/2014"];


// sorted_array_1=arr1.sort(NaturalSort);
// sorted_array_2=arr2.sort(NaturalSort);
// sorted_array_3=arr3..sort(NaturalSort);
