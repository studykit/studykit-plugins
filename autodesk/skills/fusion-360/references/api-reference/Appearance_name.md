# Appearance.name Property

Parent Object: [Appearance](Appearance.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/Appearance.h>

## Description

Returns the name of this Appearance. This is the localized name shown in the UI.

## Syntax

* [Python](#Python)
* [C++](#C++)

"appearance\_var" is a variable referencing an Appearance object. |

"appearance\_var" is a variable referencing an Appearance object. ```` ``` #include <Core/Materials/Appearance.h>  // Get the value of the property. string propertyValue = appearance_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = appearance_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Material API Sample](MaterialSample_Sample.htm) | Demonstrates using materials and appearance using the API.  To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. The sample also used an external appearance library which you can get [here](../ExtraFiles/APISampleMaterialLibrary2.adsklib). Copy that to any location on your computer and edit the path in the script. When running the script, have a design open that contains a body in the root component. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |