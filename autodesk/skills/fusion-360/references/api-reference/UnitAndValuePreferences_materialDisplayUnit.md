# UnitAndValuePreferences.materialDisplayUnit Property

Parent Object: [UnitAndValuePreferences](UnitAndValuePreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/UnitAndValuePreferences.h>

## Description

Gets and sets the units types to use when displaying values.

## Syntax

* [Python](#Python)
* [C++](#C++)

"unitAndValuePreferences\_var" is a variable referencing a UnitAndValuePreferences object. |

"unitAndValuePreferences\_var" is a variable referencing a UnitAndValuePreferences object. ```` ``` #include <Core/Application/UnitAndValuePreferences.h>  // Get the value of the property. MaterialDisplayUnits propertyValue = unitAndValuePreferences_var->materialDisplayUnit();  // Set the value of the property, where value_var is a MaterialDisplayUnits. bool returnValue = unitAndValuePreferences_var->materialDisplayUnit(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [MaterialDisplayUnits](MaterialDisplayUnits.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |