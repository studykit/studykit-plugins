# StitchFeature.stitchSurfaces Property

Parent Object: [StitchFeature](StitchFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/StitchFeature.h>

## Description

Gets and sets the surfaces to stitch together. In some cases the stitch operation results in faces being merged so the original faces are no longer available after the feature is created. in this case you need to reposition the timeline marker to just before this feature when the faces do exist.

## Syntax

* [Python](#Python)
* [C++](#C++)

"stitchFeature\_var" is a variable referencing a StitchFeature object.  ```` ``` # Get the value of the property. propertyValue = stitchFeature_var.stitchSurfaces  # Set the value of the property. stitchFeature_var.stitchSurfaces = propertyValue ``` ```` |

"stitchFeature\_var" is a variable referencing a StitchFeature object. ```` ``` #include <Fusion/Features/StitchFeature.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = stitchFeature_var->stitchSurfaces();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = stitchFeature_var->stitchSurfaces(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |