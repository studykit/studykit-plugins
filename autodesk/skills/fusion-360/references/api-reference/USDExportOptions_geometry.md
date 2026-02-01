# USDExportOptions.geometry Property

Parent Object: [USDExportOptions](USDExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/USDExportOptions.h>

## Description

Specifies the geometry to export. This can be an Occurrence, or the root Component. For STL, OBJ, and 3MF export, it can be a BRepBody. For DXF export, it can be a sketch of flat pattern.

## Syntax

* [Python](#Python)
* [C++](#C++)

"uSDExportOptions\_var" is a variable referencing a USDExportOptions object. |

"uSDExportOptions\_var" is a variable referencing a USDExportOptions object. ```` ``` #include <Fusion/Fusion/USDExportOptions.h>  // Get the value of the property. Ptr<Base> propertyValue = uSDExportOptions_var->geometry();  // Set the value of the property, where value_var is a Base. bool returnValue = uSDExportOptions_var->geometry(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |