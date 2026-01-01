# DXFSketchExportOptions.objectType Property

Parent Object: [DXFSketchExportOptions](DXFSketchExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/DXFSketchExportOptions.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dXFSketchExportOptions\_var" is a variable referencing a DXFSketchExportOptions object.  ```` ``` # Get the value of the property. propertyValue = dXFSketchExportOptions_var.objectType ``` ```` |

"dXFSketchExportOptions\_var" is a variable referencing a DXFSketchExportOptions object. ```` ``` #include <Fusion/Fusion/DXFSketchExportOptions.h>  // Get the value of the property. string propertyValue = dXFSketchExportOptions_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |