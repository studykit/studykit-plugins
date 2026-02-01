# DXF2DImportOptions.layers Property

Parent Object: [DXF2DImportOptions](DXF2DImportOptions.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/DXF2DImportOptions.h>

## Description

Gets and sets the names of the layers that will be imported. When the DXF2DImportOptions object is first created, the array returned is a list of all the layers in the DXF file. By default, all layers will be imported. You can set the property using a new array that contains the names of only those layers you want to import.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dXF2DImportOptions\_var" is a variable referencing a DXF2DImportOptions object. |

"dXF2DImportOptions\_var" is a variable referencing a DXF2DImportOptions object. ```` ``` #include <Core/Application/DXF2DImportOptions.h>  // Get the value of the property. std::vector<string> propertyValue = dXF2DImportOptions_var->layers();  // Set the value of the property, where value_var is a string. bool returnValue = dXF2DImportOptions_var->layers(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type string.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |