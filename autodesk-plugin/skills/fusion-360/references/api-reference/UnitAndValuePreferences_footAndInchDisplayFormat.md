# UnitAndValuePreferences.footAndInchDisplayFormat Property

Parent Object: [UnitAndValuePreferences](UnitAndValuePreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/UnitAndValuePreferences.h>

## Description

Gets and sets the foot and inch display format.

## Syntax

* [Python](#Python)
* [C++](#C++)

"unitAndValuePreferences\_var" is a variable referencing a UnitAndValuePreferences object. |

"unitAndValuePreferences\_var" is a variable referencing a UnitAndValuePreferences object. ```` ``` #include <Core/Application/UnitAndValuePreferences.h>  // Get the value of the property. FootAndInchDisplayFormats propertyValue = unitAndValuePreferences_var->footAndInchDisplayFormat();  // Set the value of the property, where value_var is a FootAndInchDisplayFormats. bool returnValue = unitAndValuePreferences_var->footAndInchDisplayFormat(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [FootAndInchDisplayFormats](FootAndInchDisplayFormats.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |