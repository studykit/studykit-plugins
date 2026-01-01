# MergeFacesFeatures.createInput Method

Parent Object: [MergeFacesFeatures](MergeFacesFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MergeFacesFeatures.h>

## Description

Creates a MergeFacesFeatureInput object for defining a simple merge face feature. Use properties and methods on this object to define the merge you want to create and then use the Add method, passing in the MergeFacesFeatureInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mergeFacesFeatures\_var" is a variable referencing a [MergeFacesFeatures](MergeFacesFeatures.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"mergeFacesFeatures\_var" is a variable referencing a [MergeFacesFeatures](MergeFacesFeatures.htm) object.  ```` ``` #include <Fusion/Features/MergeFacesFeatures.h>  // Uses no optional arguments. returnValue = mergeFacesFeatures_var->createInput(inputFaces);  // Uses optional arguments. returnValue = mergeFacesFeatures_var->createInput(inputFaces, isChainSelection); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MergeFacesFeatureInput](MergeFacesFeatureInput.htm) | Returns the newly created MergeFacesFeatureInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputFaces | BRepFace[] | An array of BRepFace objects that define the faces the merge will be performed on. The faces need to be connected and from the same body (solid or surface). |
| isChainSelection | boolean | A boolean value for setting whether or not faces that are connected and from the same body (solid or surface) will be included in the faces to merge. The default value is false.   This is an optional argument whose default value is False. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |