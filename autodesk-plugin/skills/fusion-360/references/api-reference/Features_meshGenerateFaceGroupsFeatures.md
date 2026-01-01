# Features.meshGenerateFaceGroupsFeatures Property![](../images/TestTubeLarge.png)

Parent Object: [Features](Features.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the mesh generate facegroup features within the component and supports the creation of new mesh generate facegroup features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<MeshGenerateFaceGroupsFeatures> propertyValue = features_var->meshGenerateFaceGroupsFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [MeshGenerateFaceGroupsFeatures](MeshGenerateFaceGroupsFeatures.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |