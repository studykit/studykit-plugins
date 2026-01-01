# Occurrence.appearance Property

Parent Object: [Occurrence](Occurrence.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrence.h>

## Description

Read-write property that gets and sets the appearance override for this occurrence. This property can return null indicating there is no override appearance and that the contents of the occurrence are displayed using there defined appearance. Setting the property to null will remove any override appearance for this occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrence\_var" is a variable referencing an Occurrence object. |

"occurrence\_var" is a variable referencing an Occurrence object. ```` ``` #include <Fusion/Components/Occurrence.h>  // Get the value of the property. Ptr<Appearance> propertyValue = occurrence_var->appearance();  // Set the value of the property, where value_var is an Appearance. bool returnValue = occurrence_var->appearance(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [Appearance](Appearance.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |