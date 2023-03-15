natsort.ns¶
Enum to control the natsort algorithm.

This class acts like an enum to control the natsort algorithm. The user may select several options simultaneously by or’ing the options together. For example, to choose ns.INT, ns.PATH, and ns.LOCALE, you could do ns.INT | ns.LOCALE | ns.PATH. Each function in the natsort package has an alg option that accepts this enum to allow fine control over how your input is sorted.

Each option has a shortened 1- or 2-letter form.

Note

Please read Possible Issues with humansorted() or ns.LOCALE before using ns.LOCALE.

INT, I (default)
The default - parse numbers as integers.

FLOAT, F
Tell natsort to parse numbers as floats.

UNSIGNED, U (default)
Tell natsort to ignore any sign (i.e. “-” or “+”) to the immediate left of a number. This is the default.

SIGNED, S
Tell natsort to take into account any sign (i.e. “-” or “+”) to the immediate left of a number.

REAL, R
This is a shortcut for ns.FLOAT | ns.SIGNED, which is useful when attempting to sort real numbers.

NOEXP, N
Tell natsort to not search for exponents as part of a float number. For example, with NOEXP the number “5.6E5” would be interpreted as 5.6, “E”, and 5 instead of 560000.

NUMAFTER, NA
Tell natsort to sort numbers after non-numbers. By default numbers will be ordered before non-numbers.

PATH, P
Tell natsort to interpret strings as filesystem paths, so they will be split according to the filesystem separator (i.e. ‘/’ on UNIX, ‘’ on Windows), as well as splitting on the file extension, if any. Without this, lists of file paths like ['Folder/', 'Folder (1)/', 'Folder (10)/'] will not be sorted properly; ‘Folder/’ will be placed at the end, not at the front. It is the same as setting the old as_path option to True.

COMPATIBILITYNORMALIZE, CN
Use the “NFKD” unicode normalization form on input rather than the default “NFD”. This will transform characters such as ‘⑦’ into ‘7’. Please see [https://stackoverflow.com/a/7934397/1399279](https://stackoverflow.com/a/7934397/1399279), [https://stackoverflow.com/a/7931547/1399279](https://stackoverflow.com/a/7931547/1399279), and [https://unicode.org/reports/tr15/](https://unicode.org/reports/tr15/) for full details into unicode normalization.

LOCALE, L
Tell natsort to be locale-aware when sorting. This includes both proper sorting of alphabetical characters as well as proper handling of locale-dependent decimal separators and thousands separators. This is a shortcut for ns.LOCALEALPHA | ns.LOCALENUM. Your sorting results will vary depending on your current locale.

LOCALEALPHA, LA
Tell natsort to be locale-aware when sorting, but only for alphabetical characters.

LOCALENUM, LN
Tell natsort to be locale-aware when sorting, but only for decimal separators and thousands separators.

IGNORECASE, IC
Tell natsort to ignore case when sorting. For example, ['Banana', 'apple', 'banana', 'Apple'] would be sorted as ['apple', 'Apple', 'Banana', 'banana'].

LOWERCASEFIRST, LF
Tell natsort to put lowercase letters before uppercase letters when sorting. For example, ['Banana', 'apple', 'banana', 'Apple'] would be sorted as ['apple', 'banana', 'Apple', 'Banana'] (the default order would be ['Apple', 'Banana', 'apple', 'banana'] which is the order from a purely ordinal sort). Useless when used with IGNORECASE. Please note that if used with LOCALE, this actually has the reverse effect and will put uppercase first (this is because LOCALE already puts lowercase first); you may use this to your advantage if you need to modify the order returned with LOCALE.

GROUPLETTERS, G
Tell natsort to group lowercase and uppercase letters together when sorting. For example, ['Banana', 'apple', 'banana', 'Apple'] would be sorted as ['Apple', 'apple', 'Banana', 'banana']. Useless when used with IGNORECASE; use with LOWERCASEFIRST to reverse the order of upper and lower case. Generally not needed with LOCALE.

CAPITALFIRST, C
Only used when LOCALE is enabled. Tell natsort to put all capitalized words before non-capitalized words. This is essentially the inverse of GROUPLETTERS, and is the default Python sorting behavior without LOCALE.

UNGROUPLETTERS, UG
An alias for CAPITALFIRST.

NANLAST, NL
If an NaN shows up in the input, this instructs natsort to treat these as +Infinity and place them after all the other numbers. By default, an NaN be treated as -Infinity and be placed first. Note that this None is treated like NaN internally.

PRESORT, PS
Sort the input as strings before sorting with the nasort algorithm. This can help eliminate inconsistent sorting in cases where two different strings represent the same number. For example, “a1” and “a01” both are internally represented as (“a”, “1), so without PRESORT the order of these two values would depend on the order they appeared in the input (because Python’s sorted is a stable sorting algorithm).

Notes

If you prefer to use import natsort as ns as opposed to from natsort import natsorted, ns, the ns options are available as top-level imports.
