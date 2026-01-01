# UnitAndValuePreferences.useScientficNotationAbove Property

Parent Object: [UnitAndValuePreferences](UnitAndValuePreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/UnitAndValuePreferences.h>

## Description

Gets and sets the number of whole digits that will be displayed before switching to scientific notation.

## Syntax

* [Python](#Python)
* [C++](#C++)

"unitAndValuePreferences\_var" is a variable referencing a UnitAndValuePreferences object. |

"unitAndValuePreferences\_var" is a variable referencing a UnitAndValuePreferences object. ```` ``` #include <Core/Application/UnitAndValuePreferences.h>  // Get the value of the property. integer propertyValue = unitAndValuePreferences_var->useScientficNotationAbove();  // Set the value of the property, where value_var is an integer. bool returnValue = unitAndValuePreferences_var->useScientficNotationAbove(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |