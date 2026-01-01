# Profile.profileLoops Property

Parent Object: [Profile](Profile.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Profile.h>

## Description

The loops or closed areas within this profile. There is always a single outer loop but there can be zero to many inner loops defining voids in the profile.

## Syntax

* [Python](#Python)
* [C++](#C++)

"profile\_var" is a variable referencing a Profile object. |

"profile\_var" is a variable referencing a Profile object. ```` ``` #include <Fusion/Sketch/Profile.h>  // Get the value of the property. Ptr<ProfileLoops> propertyValue = profile_var->profileLoops(); ``` ```` |

## Property Value

This is a read only property whose value is a [ProfileLoops](ProfileLoops.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |