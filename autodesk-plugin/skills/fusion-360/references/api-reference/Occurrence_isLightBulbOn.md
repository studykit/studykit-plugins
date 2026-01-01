# Occurrence.isLightBulbOn Property

Parent Object: [Occurrence](Occurrence.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrence.h>

## Description

Gets and sets if the light bulb of this occurrence as displayed in the browser is on or off. An occurrence will only be visible if the light bulb is switched on. However, the light bulb can be on and the occurrence still invisible if a higher level occurrence in the assembly context is not visible because its light bulb is off.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrence\_var" is a variable referencing an Occurrence object. |

"occurrence\_var" is a variable referencing an Occurrence object. ```` ``` #include <Fusion/Components/Occurrence.h>  // Get the value of the property. boolean propertyValue = occurrence_var->isLightBulbOn();  // Set the value of the property, where value_var is a boolean. bool returnValue = occurrence_var->isLightBulbOn(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |