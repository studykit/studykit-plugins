# ArrangeFeature.arrangeStatistics Property

Parent Object: [ArrangeFeature](ArrangeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeFeature.h>

## Description

Returns statistics about the arrangement in JSON format as a string. Each item in the JSON is identified with its English name, and the current localized name is also provided. The values follow the API rules, where all length values are in centimeters, and areas are in square centimeters. The returned JSON may include additional values in the future, so code consuming this output should be tolerant of new fields.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeFeature\_var" is a variable referencing an ArrangeFeature object. |

"arrangeFeature\_var" is a variable referencing an ArrangeFeature object. ```` ``` #include <Fusion/Arrange/ArrangeFeature.h>  // Get the value of the property. string propertyValue = arrangeFeature_var->arrangeStatistics(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |