# Occurrence.isIsolated Property

Parent Object: [Occurrence](Occurrence.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrence.h>

## Description

Gets and sets whether this occurrence is isolated in the UI. When an occurrence is isolated it is the only one visible in the user-interface. Only one occurrence can be isolated at a time so setting this property to true will un-isolate an occurrence that is currently isolated. Setting this property to false for an occurrence that is current isolated will un-isolate it so that no occurrence will be isolated.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrence\_var" is a variable referencing an Occurrence object. |

"occurrence\_var" is a variable referencing an Occurrence object. ```` ``` #include <Fusion/Components/Occurrence.h>  // Get the value of the property. boolean propertyValue = occurrence_var->isIsolated();  // Set the value of the property, where value_var is a boolean. bool returnValue = occurrence_var->isIsolated(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |