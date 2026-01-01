# UnitAndValuePreferences.minimumPrecisionWhenHidingZeros Property

Parent Object: [UnitAndValuePreferences](UnitAndValuePreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/UnitAndValuePreferences.h>

## Description

Gets and sets the minimum number of digits to the right of the decimal to display before hiding trailing zeros.

## Syntax

* [Python](#Python)
* [C++](#C++)

"unitAndValuePreferences\_var" is a variable referencing a UnitAndValuePreferences object. |

"unitAndValuePreferences\_var" is a variable referencing a UnitAndValuePreferences object. ```` ``` #include <Core/Application/UnitAndValuePreferences.h>  // Get the value of the property. integer propertyValue = unitAndValuePreferences_var->minimumPrecisionWhenHidingZeros();  // Set the value of the property, where value_var is an integer. bool returnValue = unitAndValuePreferences_var->minimumPrecisionWhenHidingZeros(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |