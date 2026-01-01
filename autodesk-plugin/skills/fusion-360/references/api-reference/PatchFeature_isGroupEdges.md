# PatchFeature.isGroupEdges Property

Parent Object: [PatchFeature](PatchFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatchFeature.h>

## Description

Gets and sets if the edges in the boundary curve are treated as a group , and they all use the same continuity. If this property is True (which is the default), the continuity for all edges is controlled by the continuity property. If this property is false; the continuity is set for each edge using the setContinuity method.

## Syntax

* [Python](#Python)
* [C++](#C++)

"patchFeature\_var" is a variable referencing a PatchFeature object.  ```` ``` # Get the value of the property. propertyValue = patchFeature_var.isGroupEdges  # Set the value of the property. patchFeature_var.isGroupEdges = propertyValue ``` ```` |

"patchFeature\_var" is a variable referencing a PatchFeature object. ```` ``` #include <Fusion/Features/PatchFeature.h>  // Get the value of the property. boolean propertyValue = patchFeature_var->isGroupEdges();  // Set the value of the property, where value_var is a boolean. bool returnValue = patchFeature_var->isGroupEdges(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |