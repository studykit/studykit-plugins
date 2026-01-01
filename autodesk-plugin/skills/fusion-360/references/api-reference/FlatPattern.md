# FlatPattern Object

Derived from: [Feature](Feature.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPattern.h>

## Description

The FlatPattern object provides access to the flattened representation of a folded part. This supports most of the functionality of a regular component like creating sketches, construction geometry, and most features. Functionality that is not supported in a flat pattern will fail if you attempt to use it. For example, the creation of occurrences and new components is not supported. Also the creation of sheet metal features is not supported.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](FlatPattern_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](FlatPattern_deleteMe.htm) | Deletes the feature. This works for both parametric and non-parametric features. |
| [dissolve](FlatPattern_dissolve.htm) | Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features. |
| [getBendInfo](FlatPattern_getBendInfo.htm) | Returns bend information for the specified bend. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](FlatPattern_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](FlatPattern_attributes.htm) | Returns the collection of attributes associated with this face. |
| [baseFeature](FlatPattern_baseFeature.htm) | If this feature is associated with a base feature, this property will return that base feature. If it's not associated with a base feature, this property will return null. |
| [bendLinesBody](FlatPattern_bendLinesBody.htm) | Returns the wire B-Rep body that represents the bend lines of the flattened sheet metal part. |
| [bodies](FlatPattern_bodies.htm) | Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features. |
| [bottomFace](FlatPattern_bottomFace.htm) | Returns the "bottom" face of the flat pattern B-Rep body. |
| [entityToken](FlatPattern_entityToken.htm) | Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.   When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them. |
| [errorOrWarningMessage](FlatPattern_errorOrWarningMessage.htm) | Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string. |
| [extentLinesBody](FlatPattern_extentLinesBody.htm) | Returns the wire B-Rep body that represents the extent lines of the flattened sheet metal part. |
| [faces](FlatPattern_faces.htm) | Returns the faces that were created by this feature. This works for both parametric and non-parametric features.   Depending on the modifications made to the body after the feature was created, this may not return all of the faces. For example, when a component is created from a body, the original body and its faces no longer exist, so this won't return any faces. However, you can roll the timeline to immediately after the feature, and all the original faces will be available. |
| [flatBody](FlatPattern_flatBody.htm) | Returns the B-Rep body that represents the flattened sheet metal part. |
| [foldedBody](FlatPattern_foldedBody.htm) | Returns the folded B-Rep body in the design that this flat pattern was created from. |
| [healthState](FlatPattern_healthState.htm) | Returns the current health state of the feature. |
| [isParametric](FlatPattern_isParametric.htm) | Indicates if this feature is parametric or not. |
| [isSuppressed](FlatPattern_isSuppressed.htm) | Gets and sets if this feature is suppressed. This is only valid for parametric features. |
| [isValid](FlatPattern_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [linkedFeatures](FlatPattern_linkedFeatures.htm) | Returns the set of features that are linked to this feature. The set of linked features are all of the features that were created in various components as the result of a single feature being created in the user interface. |
| [name](FlatPattern_name.htm) | Returns the name of the feature as seen in the browser (non-parametric) or in the timeline (parametric). |
| [objectType](FlatPattern_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentComponent](FlatPattern_parentComponent.htm) | Returns the parent component that owns this feature. |
| [sideFaces](FlatPattern_sideFaces.htm) | Returns the "side" faces of the flat pattern B-Rep body. These are the faces around the edge of the flat pattern that connect the top and bottom faces. |
| [timelineObject](FlatPattern_timelineObject.htm) | Returns the timeline object associated with this feature. |
| [topFace](FlatPattern_topFace.htm) | Returns the "top" face of the flat pattern B-Rep body. |

## Accessed From

[Component.createFlatPattern](Component_createFlatPattern.htm), [Component.flatPattern](Component_flatPattern.htm), [FlatPatternComponent.createFlatPattern](FlatPatternComponent_createFlatPattern.htm), [FlatPatternComponent.flatPattern](FlatPatternComponent_flatPattern.htm), [FlatPatternProduct.flatPattern](FlatPatternProduct_flatPattern.htm)

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |