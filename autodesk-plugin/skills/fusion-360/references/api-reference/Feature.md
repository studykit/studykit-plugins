# Feature Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Feature.h>

## Description

Base class object representing all features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Feature_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](Feature_deleteMe.htm) | Deletes the feature. This works for both parametric and non-parametric features. |
| [dissolve](Feature_dissolve.htm) | Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](Feature_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](Feature_attributes.htm) | Returns the collection of attributes associated with this face. |
| [baseFeature](Feature_baseFeature.htm) | If this feature is associated with a base feature, this property will return that base feature. If it's not associated with a base feature, this property will return null. |
| [bodies](Feature_bodies.htm) | Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features. |
| [entityToken](Feature_entityToken.htm) | Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.   When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them. |
| [errorOrWarningMessage](Feature_errorOrWarningMessage.htm) | Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string. |
| [faces](Feature_faces.htm) | Returns the faces that were created by this feature. This works for both parametric and non-parametric features.   Depending on the modifications made to the body after the feature was created, this may not return all of the faces. For example, when a component is created from a body, the original body and its faces no longer exist, so this won't return any faces. However, you can roll the timeline to immediately after the feature, and all the original faces will be available. |
| [healthState](Feature_healthState.htm) | Returns the current health state of the feature. |
| [isParametric](Feature_isParametric.htm) | Indicates if this feature is parametric or not. |
| [isSuppressed](Feature_isSuppressed.htm) | Gets and sets if this feature is suppressed. This is only valid for parametric features. |
| [isValid](Feature_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [linkedFeatures](Feature_linkedFeatures.htm) | Returns the set of features that are linked to this feature. The set of linked features are all of the features that were created in various components as the result of a single feature being created in the user interface. |
| [name](Feature_name.htm) | Returns the name of the feature as seen in the browser (non-parametric) or in the timeline (parametric). |
| [objectType](Feature_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentComponent](Feature_parentComponent.htm) | Returns the parent component that owns this feature. |
| [timelineObject](Feature_timelineObject.htm) | Returns the timeline object associated with this feature. |

## Accessed From

[AllExtentDefinition.parentFeature](AllExtentDefinition_parentFeature.htm), [AngleExtentDefinition.parentFeature](AngleExtentDefinition_parentFeature.htm), [DistanceExtentDefinition.parentFeature](DistanceExtentDefinition_parentFeature.htm), [ExtentDefinition.parentFeature](ExtentDefinition_parentFeature.htm), [FeatureList.item](FeatureList_item.htm), [Features.item](Features_item.htm), [Features.itemByName](Features_itemByName.htm), [FromEntityStartDefinition.parentFeature](FromEntityStartDefinition_parentFeature.htm), [OffsetStartDefinition.parentFeature](OffsetStartDefinition_parentFeature.htm), [OneSideToExtentDefinition.parentFeature](OneSideToExtentDefinition_parentFeature.htm), [PatternElement.parentFeature](PatternElement_parentFeature.htm), [ProfilePlaneStartDefinition.parentFeature](ProfilePlaneStartDefinition_parentFeature.htm), [SymmetricExtentDefinition.parentFeature](SymmetricExtentDefinition_parentFeature.htm), [ThroughAllExtentDefinition.parentFeature](ThroughAllExtentDefinition_parentFeature.htm), [ToEntityExtentDefinition.parentFeature](ToEntityExtentDefinition_parentFeature.htm), [TwoSidesAngleExtentDefinition.parentFeature](TwoSidesAngleExtentDefinition_parentFeature.htm), [TwoSidesDistanceExtentDefinition.parentFeature](TwoSidesDistanceExtentDefinition_parentFeature.htm), [TwoSidesToExtentDefinition.parentFeature](TwoSidesToExtentDefinition_parentFeature.htm)

## Derived Classes

[ArrangeFeature](ArrangeFeature.htm), [BaseFeature](BaseFeature.htm), [BossFeature](BossFeature.htm), [BoundaryFillFeature](BoundaryFillFeature.htm), [BoxFeature](BoxFeature.htm), [ChamferFeature](ChamferFeature.htm), [CircularPatternFeature](CircularPatternFeature.htm), [CoilFeature](CoilFeature.htm), [CombineFeature](CombineFeature.htm), [CopyPasteBody](CopyPasteBody.htm), [CustomFeature](CustomFeature.htm), [CutPasteBody](CutPasteBody.htm), [CylinderFeature](CylinderFeature.htm), [DeleteFaceFeature](DeleteFaceFeature.htm), [DraftFeature](DraftFeature.htm), [EmbossFeature](EmbossFeature.htm), [ExtendFeature](ExtendFeature.htm), [ExtrudeFeature](ExtrudeFeature.htm), [FilletFeature](FilletFeature.htm), [FlangeFeature](FlangeFeature.htm), [FlatPattern](FlatPattern.htm), [FormFeature](FormFeature.htm), [HoleFeature](HoleFeature.htm), [LoftFeature](LoftFeature.htm), [MeshConvertFeature](MeshConvertFeature.htm), [MeshFeature](MeshFeature.htm), [MirrorFeature](MirrorFeature.htm), [MoveFeature](MoveFeature.htm), [OffsetFacesFeature](OffsetFacesFeature.htm), [OffsetFeature](OffsetFeature.htm), [PatchFeature](PatchFeature.htm), [PathPatternFeature](PathPatternFeature.htm), [PipeFeature](PipeFeature.htm), [RectangularPatternFeature](RectangularPatternFeature.htm), [RefoldFeature](RefoldFeature.htm), [RemoveFeature](RemoveFeature.htm), [ReplaceFaceFeature](ReplaceFaceFeature.htm), [ReverseNormalFeature](ReverseNormalFeature.htm), [RevolveFeature](RevolveFeature.htm), [RibFeature](RibFeature.htm), [RipFeature](RipFeature.htm), [RuledSurfaceFeature](RuledSurfaceFeature.htm), [RuleFilletFeature](RuleFilletFeature.htm), [ScaleFeature](ScaleFeature.htm), [ShellFeature](ShellFeature.htm), [SilhouetteSplitFeature](SilhouetteSplitFeature.htm), [SphereFeature](SphereFeature.htm), [SplitBodyFeature](SplitBodyFeature.htm), [SplitFaceFeature](SplitFaceFeature.htm), [StitchFeature](StitchFeature.htm), [SurfaceDeleteFaceFeature](SurfaceDeleteFaceFeature.htm), [SweepFeature](SweepFeature.htm), [ThickenFeature](ThickenFeature.htm), [ThreadFeature](ThreadFeature.htm), [TorusFeature](TorusFeature.htm), [TrimFeature](TrimFeature.htm), [UnfoldFeature](UnfoldFeature.htm), [UnstitchFeature](UnstitchFeature.htm), [UntrimFeature](UntrimFeature.htm), [VolumetricCustomFeature](VolumetricCustomFeature.htm), [VolumetricModelToMeshFeature](VolumetricModelToMeshFeature.htm), [WebFeature](WebFeature.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |