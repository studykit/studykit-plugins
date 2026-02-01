# MeshConvertFeature Object ![Preview](../images/TestTubeLarge.png)

Derived from: [Feature](Feature.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshConvertFeature.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

Object that represents an existing mesh convert feature in a design. To change the properties of this feature, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MeshConvertFeature_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](MeshConvertFeature_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [deleteMe](MeshConvertFeature_deleteMe.htm) | Deletes the feature. This works for both parametric and non-parametric features. |
| [dissolve](MeshConvertFeature_dissolve.htm) | Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](MeshConvertFeature_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](MeshConvertFeature_attributes.htm) | Returns the collection of attributes associated with this face. |
| [baseFeature](MeshConvertFeature_baseFeature.htm) | If this feature is associated with a base feature, this property will return that base feature. If it's not associated with a base feature, this property will return null. |
| [bodies](MeshConvertFeature_bodies.htm) | Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features. |
| [entityToken](MeshConvertFeature_entityToken.htm) | Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.   When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them. |
| [errorOrWarningMessage](MeshConvertFeature_errorOrWarningMessage.htm) | Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string. |
| [faces](MeshConvertFeature_faces.htm) | Returns the faces that were created by this feature. This works for both parametric and non-parametric features.   Depending on the modifications made to the body after the feature was created, this may not return all of the faces. For example, when a component is created from a body, the original body and its faces no longer exist, so this won't return any faces. However, you can roll the timeline to immediately after the feature, and all the original faces will be available. |
| [healthState](MeshConvertFeature_healthState.htm) | Returns the current health state of the feature. |
| [inputBodies](MeshConvertFeature_inputBodies.htm) | Gets and sets the input meshes. |
| [isParametric](MeshConvertFeature_isParametric.htm) | Indicates if this feature is parametric or not. |
| [isPreprocessHoles](MeshConvertFeature_isPreprocessHoles.htm) | Smooths the boundaries of open holes in the mesh body. Improves the chance of successful conversion by refining the shape of holes that will remain open. Only valid if meshConvertMethodType is OrganicMeshConvertMethodType. |
| [isSuppressed](MeshConvertFeature_isSuppressed.htm) | Gets and sets if this feature is suppressed. This is only valid for parametric features. |
| [isValid](MeshConvertFeature_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [linkedFeatures](MeshConvertFeature_linkedFeatures.htm) | Returns the set of features that are linked to this feature. The set of linked features are all of the features that were created in various components as the result of a single feature being created in the user interface. |
| [meshConvertAccuracyType](MeshConvertFeature_meshConvertAccuracyType.htm) | Gets and sets the accuracy of organic mesh convert. Only valid if meshConvertResolutionType is ByAccuracyMeshConvertResolutionType. |
| [meshConvertMethodType](MeshConvertFeature_meshConvertMethodType.htm) | Gets and sets the convert type of mesh convert. |
| [meshConvertResolutionType](MeshConvertFeature_meshConvertResolutionType.htm) | Gets and sets the resolution method of mesh convert. Only valid if meshConvertMethodType is OrganicMeshConvertMethodType. |
| [name](MeshConvertFeature_name.htm) | Returns the name of the feature as seen in the browser (non-parametric) or in the timeline (parametric). |
| [nativeObject](MeshConvertFeature_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [numberOfFaces](MeshConvertFeature_numberOfFaces.htm) | Specify the number of faces to generate for the converted body. Only valid if meshConvertResolutionTypes is ByFacetNumberMeshConvertResolutionType. |
| [objectType](MeshConvertFeature_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentComponent](MeshConvertFeature_parentComponent.htm) | Returns the parent component that owns this feature. |
| [timelineObject](MeshConvertFeature_timelineObject.htm) | Returns the timeline object associated with this feature. |

## Accessed From

[MeshConvertFeature.createForAssemblyContext](MeshConvertFeature_createForAssemblyContext.htm), [MeshConvertFeature.nativeObject](MeshConvertFeature_nativeObject.htm), [MeshConvertFeatures.add](MeshConvertFeatures_add.htm), [MeshConvertFeatures.item](MeshConvertFeatures_item.htm), [MeshConvertFeatures.itemByName](MeshConvertFeatures_itemByName.htm)

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |