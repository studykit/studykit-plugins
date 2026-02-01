# Data.personalUseLimits Property

Parent Object: [Data](Data.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/Data.h>

## Description

If the user is running with a "Fusion for Personal Use license", this property will return a peronalUseLimits object which provides information about file limits associated with the license. If the user is running with any other license type, this property will return null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"data\_var" is a variable referencing a Data object. |

"data\_var" is a variable referencing a Data object. ```` ``` #include <Core/Dashboard/Data.h>  // Get the value of the property. Ptr<PersonalUseLimits> propertyValue = data_var->personalUseLimits(); ``` ```` |

## Property Value

This is a read only property whose value is a [PersonalUseLimits](PersonalUseLimits.htm).

## Version

Introduced in version May 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |