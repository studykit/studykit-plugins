# C3MFExportOptions.geometry Property

Parent Object: [C3MFExportOptions](C3MFExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/C3MFExportOptions.h>

## Description

Specifies the geometry to export. This can be an Occurrence, or the root Component. For STL, OBJ, and 3MF export, it can be a BRepBody. For DXF export, it can be a sketch of flat pattern.

## Syntax

* [Python](#Python)
* [C++](#C++)

"c3MFExportOptions\_var" is a variable referencing a C3MFExportOptions object. |

"c3MFExportOptions\_var" is a variable referencing a C3MFExportOptions object. ```` ``` #include <Fusion/Fusion/C3MFExportOptions.h>  // Get the value of the property. Ptr<Base> propertyValue = c3MFExportOptions_var->geometry();  // Set the value of the property, where value_var is a Base. bool returnValue = c3MFExportOptions_var->geometry(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version September 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |