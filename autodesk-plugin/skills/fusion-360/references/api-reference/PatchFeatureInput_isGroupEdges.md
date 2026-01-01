# PatchFeatureInput.isGroupEdges Property

Parent Object: [PatchFeatureInput](PatchFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatchFeatureInput.h>

## Description

Gets and sets if the edges in the boundary curve are treated as a group, and they all use the same continuity. If this property is True (which is the default), the continuity property controls the continuity for all edges. If this property is false; the continuity is set for each edge using the setContinuity method.

## Syntax

* [Python](#Python)
* [C++](#C++)

"patchFeatureInput\_var" is a variable referencing a PatchFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = patchFeatureInput_var.isGroupEdges  # Set the value of the property. patchFeatureInput_var.isGroupEdges = propertyValue ``` ```` |

"patchFeatureInput\_var" is a variable referencing a PatchFeatureInput object. ```` ``` #include <Fusion/Features/PatchFeatureInput.h>  // Get the value of the property. boolean propertyValue = patchFeatureInput_var->isGroupEdges();  // Set the value of the property, where value_var is a boolean. bool returnValue = patchFeatureInput_var->isGroupEdges(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |