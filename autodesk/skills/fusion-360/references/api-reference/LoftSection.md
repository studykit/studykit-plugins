# LoftSection Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftSection.h>

## Description

A single loft section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](LoftSection_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](LoftSection_deleteMe.htm) | Deletes this LoftSection. |
| [reorder](LoftSection_reorder.htm) | Repositions this section so that it has the new index specified.   If this LoftSection object is associated with a created feature, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [setDirectionEndCondition](LoftSection_setDirectionEndCondition.htm) | Sets the end condition to be defined by a direction and weight.   This is valid for sections defined with sketch curves.   If this LoftSection object is associated with a created feature, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [setFreeEndCondition](LoftSection_setFreeEndCondition.htm) | Sets the end condition to be a "Free" end condition. This is the default end condition when a new section is added.   This is valid for sections defined with all curve types.   If this LoftSection object is associated with a created feature, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [setPointSharpEndCondition](LoftSection_setPointSharpEndCondition.htm) | Sets the end condition to be sharp where the section is a point. This is the default condition for a point section.   If this LoftSection object is associated with a created feature, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [setPointTangentEndCondition](LoftSection_setPointTangentEndCondition.htm) | Set the end condition to a tangent condition in the case where the section is a point.   If this LoftSection object is associated with a created feature, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [setSmoothEndCondition](LoftSection_setSmoothEndCondition.htm) | Sets the end condition to be smooth to the adjacent face. If the end profile is not defined by a BRepEdge, then this is ignored because there is no face to be smooth to.   This is only valid on the first or last section.   If this LoftSection object is associated with a created feature, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [setTangentEndCondition](LoftSection_setTangentEndCondition.htm) | Sets the end condition to be tangent to the adjacent face. If the section is not defined by a BRepEdge, then this is ignored because there is no face to be tangent to.   This is only valid on the first or last profile.   If this LoftSection object is associated with a created feature, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [endCondition](LoftSection_endCondition.htm) | Returns the current end condition. This is only valid for the first and last section and when the result is not closed. In other cases this will return null. This returns one of the several objects derived from LoftEndCondition and represents the current end condition. You can edit the existing condition using properties on the returned object. You can change the end condition using one of the set methods on the LoftSection object.   If this LoftSection object is associated with a created feature, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [entity](LoftSection_entity.htm) | Get and sets the entity that defines the section of the loft. This can be a BRepFace, Profile, Path, SketchPoint, ConstructionPoint, or an ObjectCollection of contiguous profiles.   If this LoftSection object is associated with a created feature, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [index](LoftSection_index.htm) | The position of this LoftSection within the collection. The first section has an index of 0. This is also the order of how the section will be used in the loft. The order can be modified by using the reorder method. |
| [isValid](LoftSection_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](LoftSection_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |

## Accessed From

[LoftDirectionEndCondition.parentLoftSection](LoftDirectionEndCondition_parentLoftSection.htm), [LoftEndCondition.parentLoftSection](LoftEndCondition_parentLoftSection.htm), [LoftFreeEndCondition.parentLoftSection](LoftFreeEndCondition_parentLoftSection.htm), [LoftPointSharpEndCondition.parentLoftSection](LoftPointSharpEndCondition_parentLoftSection.htm), [LoftPointTangentEndCondition.parentLoftSection](LoftPointTangentEndCondition_parentLoftSection.htm), [LoftSections.add](LoftSections_add.htm), [LoftSections.item](LoftSections_item.htm), [LoftSmoothEndCondition.parentLoftSection](LoftSmoothEndCondition_parentLoftSection.htm), [LoftTangentEndCondition.parentLoftSection](LoftTangentEndCondition_parentLoftSection.htm)

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |