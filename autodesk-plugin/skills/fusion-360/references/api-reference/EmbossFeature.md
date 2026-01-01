# EmbossFeature Object ![Preview](../images/TestTubeLarge.png)

Derived from: [Feature](Feature.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/EmbossFeature.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

Object that represents an existing emboss feature in a design.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](EmbossFeature_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](EmbossFeature_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [deleteMe](EmbossFeature_deleteMe.htm) | Deletes the feature. This works for both parametric and non-parametric features. |
| [dissolve](EmbossFeature_dissolve.htm) | Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](EmbossFeature_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](EmbossFeature_attributes.htm) | Returns the collection of attributes associated with this face. |
| [baseFeature](EmbossFeature_baseFeature.htm) | If this feature is associated with a base feature, this property will return that base feature. If it's not associated with a base feature, this property will return null. |
| [bodies](EmbossFeature_bodies.htm) | Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features. |
| [depth](EmbossFeature_depth.htm) | Returns the parameter that controls the depth of the emboss. A positive value results in the emboss protruding out of the body and the negative value results in the emboss going into the body. To edit the depth, use properties on the returned ModelParameter. |
| [entityToken](EmbossFeature_entityToken.htm) | Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.   When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them. |
| [errorOrWarningMessage](EmbossFeature_errorOrWarningMessage.htm) | Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string. |
| [faces](EmbossFeature_faces.htm) | Returns the faces that were created by this feature. This works for both parametric and non-parametric features.   Depending on the modifications made to the body after the feature was created, this may not return all of the faces. For example, when a component is created from a body, the original body and its faces no longer exist, so this won't return any faces. However, you can roll the timeline to immediately after the feature, and all the original faces will be available. |
| [healthState](EmbossFeature_healthState.htm) | Returns the current health state of the feature. |
| [horizontalDistance](EmbossFeature_horizontalDistance.htm) | Returns the parameter that controls the horizontal offset distance. To edit the offset, use properties on the returned ModelParameter. |
| [inputFaces](EmbossFeature_inputFaces.htm) | Gets and sets an array of BRepFace objects that define the faces the emboss will be performed on. The value of the isTangentChain property controls if faces that are tangent to any of the specified faces are also included.   To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [isParametric](EmbossFeature_isParametric.htm) | Indicates if this feature is parametric or not. |
| [isSuppressed](EmbossFeature_isSuppressed.htm) | Gets and sets if this feature is suppressed. This is only valid for parametric features. |
| [isTangentChain](EmbossFeature_isTangentChain.htm) | Gets and sets whether any faces that are tangentially connected to any of the input faces will also be used.   To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [isValid](EmbossFeature_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [linkedFeatures](EmbossFeature_linkedFeatures.htm) | Returns the set of features that are linked to this feature. The set of linked features are all of the features that were created in various components as the result of a single feature being created in the user interface. |
| [name](EmbossFeature_name.htm) | Returns the name of the feature as seen in the browser (non-parametric) or in the timeline (parametric). |
| [nativeObject](EmbossFeature_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of its parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](EmbossFeature_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentComponent](EmbossFeature_parentComponent.htm) | Returns the parent component that owns this feature. |
| [profiles](EmbossFeature_profiles.htm) | Gets and sets the set Profile objects that define the shape of the emboss. The profile argument can be Profile and SketchText objects. When multiple objects are used, all profiles and sketch texts must be co-planar.   To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [rotationAngle](EmbossFeature_rotationAngle.htm) | Returns the parameter that controls the rotation angle. To edit the angle, use properties on the returned ModelParameter. |
| [timelineObject](EmbossFeature_timelineObject.htm) | Returns the timeline object associated with this feature. |
| [verticalDistance](EmbossFeature_verticalDistance.htm) | Returns the parameter that controls the vertical offset distance. To edit the offset, use properties on the returned ModelParameter. |

## Accessed From

[EmbossFeature.createForAssemblyContext](EmbossFeature_createForAssemblyContext.htm), [EmbossFeature.nativeObject](EmbossFeature_nativeObject.htm), [EmbossFeatures.add](EmbossFeatures_add.htm), [EmbossFeatures.item](EmbossFeatures_item.htm), [EmbossFeatures.itemByName](EmbossFeatures_itemByName.htm)

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |