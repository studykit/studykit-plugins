# WorkPlaneProxy Object

Derived from: [WorkPlane](../WorkPlane/WorkPlane.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../WorkPlaneProxy/WorkPlaneProxy_Delete.md) | Method that deletes the work plane. Optionally the dependent objects will be deleted. This method will fail in the case where this object was created as a result of a derived part. The HasReferenceComponent property can be used to determine when this is the case. |
| [FlipNormal](../WorkPlaneProxy/WorkPlaneProxy_FlipNormal.md) | Method that reverses the normal of the work plane. The current normal direction can be determined by using the Plane object returned by Plane property of the work plane. |
| [GetPosition](../WorkPlaneProxy/WorkPlaneProxy_GetPosition.md) | Method that returns the position and orientation of a work plane. When sketches are created on a work plane they inherit the work plane's origin and orientation. This method is useful to predetermine what the orientation will be before the sketch is created. |
| [GetReferenceKey](../WorkPlaneProxy/WorkPlaneProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSize](../WorkPlaneProxy/WorkPlaneProxy_GetSize.md) | Method that gets the current size of the displayed graphics for the work plane. The returned points are in the coordinate space of the workplane. |
| [SetByLineAndTangent](../WorkPlaneProxy/WorkPlaneProxy_SetByLineAndTangent.md) | Method that redefines the work plane to be through the input line and tangent to the input surface. |
| [SetByLinePlaneAndAngle](../WorkPlaneProxy/WorkPlaneProxy_SetByLinePlaneAndAngle.md) | Method that redefines the work plane to be through the input line at the specified angle from the input plane. |
| [SetByNormalToCurve](../WorkPlaneProxy/WorkPlaneProxy_SetByNormalToCurve.md) | Method that redefines the work plane to pass through the input point and normal to the input curve. |
| [SetByPlaneAndOffset](../WorkPlaneProxy/WorkPlaneProxy_SetByPlaneAndOffset.md) | Method that redefines the work plane to be parallel to the input plane at a specified distance in the specified direction. |
| [SetByPlaneAndPoint](../WorkPlaneProxy/WorkPlaneProxy_SetByPlaneAndPoint.md) | Method that redefines the work plane to be parallel to the input plane and passing through the input point. |
| [SetByPlaneAndTangent](../WorkPlaneProxy/WorkPlaneProxy_SetByPlaneAndTangent.md) | Method that redefines the work plane to be parallel to the input plane and tangent to the input surface. |
| [SetByPointAndTangent](../WorkPlaneProxy/WorkPlaneProxy_SetByPointAndTangent.md) | Method that redefines the work plane to pass through the input point and tangent to the input surface. |
| [SetByThreePoints](../WorkPlaneProxy/WorkPlaneProxy_SetByThreePoints.md) | Method that redefines the work plane to be based on the three input points. |
| [SetByTorusMidPlane](../WorkPlaneProxy/WorkPlaneProxy_SetByTorusMidPlane.md) | Method that redefines the work plane to be at the mid-plane of the torus specified by the input face. |
| [SetByTwoLines](../WorkPlaneProxy/WorkPlaneProxy_SetByTwoLines.md) | Method that redefines the work plane to be based on the two input lines. |
| [SetByTwoPlanes](../WorkPlaneProxy/WorkPlaneProxy_SetByTwoPlanes.md) | Method that redefines a bisection work plane to be based on the two planes. |
| [SetEndOfPart](../WorkPlaneProxy/WorkPlaneProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. The argument defines if the end-of-part marker will be positioned just before or just after the object. If the object is contained within another object and is not in the top level of the browser, the positioning of the marker will be relative to the top-level object the calling object is contained within. An example of this case is a sketch that has not been shared and has been consumed by a feature. Another example is a nested work feature. |
| [SetFixed](../WorkPlaneProxy/WorkPlaneProxy_SetFixed.md) | Method that redefines the work plane at the position and orientation defined by the point and X and Y axis vectors. |
| [SetSize](../WorkPlaneProxy/WorkPlaneProxy_SetSize.md) | Method that sets the current size of the displayed graphics for the work plane. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../WorkPlaneProxy/WorkPlaneProxy_Adaptive.md) | Specifies whether the work plane is adaptive. |
| [Application](../WorkPlaneProxy/WorkPlaneProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../WorkPlaneProxy/WorkPlaneProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [AutoResize](../WorkPlaneProxy/WorkPlaneProxy_AutoResize.md) | Gets and sets whether this work plane should be resized automatically based on the component size. |
| [Construction](../WorkPlaneProxy/WorkPlaneProxy_Construction.md) | Boolean property that returns whether the work plane is a construction work plane or not. A construction work plane is hidden from the user and is not displayed graphically or listed in the browser. Some properties and methods of the WorkPlane object will behave differently for a construction work plane. These are Adaptive, Name, Visible, GetSize, and SetSize. |
| [Consumed](../WorkPlaneProxy/WorkPlaneProxy_Consumed.md) | Gets whether the WorkPlane is consumed or not. |
| [ConsumeInputs](../WorkPlaneProxy/WorkPlaneProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ContainingOccurrence](../WorkPlaneProxy/WorkPlaneProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Definition](../WorkPlaneProxy/WorkPlaneProxy_Definition.md) | Property that returns one of the work plane definition objects. Which definition object returned will depend on how the work plane is defined. The DefinitionType property can be used to determine the type of definition the Definition property will return. |
| [DefinitionType](../WorkPlaneProxy/WorkPlaneProxy_DefinitionType.md) | Property that returns the type of definition that is used to define the work plane. This can be kThreePointsWorkPlane, kTwoLinesWorkPlane, kLineAndPointWorkPlane, kPlaneAndPointWorkPlane, kLinePlaneAndAngleWorkPlane, kPlaneAndOffsetWorkPlane, kLineAndTangentWorkPlane, kPlaneAndTangentWorkPlane, kSketchWorkPlane, kFixedWorkPlane, kNormalToCurveWorkPlane, kTwoPlanesWorkPlane, kTorusMidPlaneWorkPlane, or AssemblyWorkPlane. |
| [Dependents](../WorkPlaneProxy/WorkPlaneProxy_Dependents.md) | Property that returns the collection of objects that have a direct dependency on the work plane. |
| [DrivenBy](../WorkPlaneProxy/WorkPlaneProxy_DrivenBy.md) | Property that returns the collection of objects that the work plane is dependent on. |
| [Exported](../WorkPlaneProxy/WorkPlaneProxy_Exported.md) | Read-write property that gets and sets whether the object is exported. Objects must be marked for export in order for them to be derived. |
| [Grounded](../WorkPlaneProxy/WorkPlaneProxy_Grounded.md) | Gets/Sets the Boolean flag that specifies whether this work plane is grounded or not. |
| [HasReferenceComponent](../WorkPlaneProxy/WorkPlaneProxy_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [HealthStatus](../WorkPlaneProxy/WorkPlaneProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsCoordinateSystemElement](../WorkPlaneProxy/WorkPlaneProxy_IsCoordinateSystemElement.md) | Property that returns whether the work plane belongs to a coordinate system. If so, edits and delete are not allowed. |
| [IsOwnedByFeature](../WorkPlaneProxy/WorkPlaneProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [IsParentSketch](../WorkPlaneProxy/WorkPlaneProxy_IsParentSketch.md) | Property that indicates whether the work plane belongs to a 3d sketch. |
| [IsPatternElement](../WorkPlaneProxy/WorkPlaneProxy_IsPatternElement.md) | Property that gets whether the work plane was created by a pattern. If so, edits and delete are not allowed. |
| [Name](../WorkPlaneProxy/WorkPlaneProxy_Name.md) | Specifies the name of the work plane. |
| [NativeObject](../WorkPlaneProxy/WorkPlaneProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../WorkPlaneProxy/WorkPlaneProxy_OwnedBy.md) | Read-only property that returns the client feature that owns this object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parent](../WorkPlaneProxy/WorkPlaneProxy_Parent.md) | Property returning the parent  object. |
| [ParentSketch](../WorkPlaneProxy/WorkPlaneProxy_ParentSketch.md) | Gets the parent 3d sketch if this work plane belongs to a 3d sketch, Gets Nothing otherwise. |
| [Plane](../WorkPlaneProxy/WorkPlaneProxy_Plane.md) | Property that returns a Plane's geometry. The Plane object returned provides information about the position and normal of the work plane. |
| [ReferenceComponent](../WorkPlaneProxy/WorkPlaneProxy_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../WorkPlaneProxy/WorkPlaneProxy_ReferencedEntity.md) | Property that returns the referenced WorkPlane in the case where this work plane was created using a referenced component. An example of this is when a work plane is selected as part of a derived part. The HasReferenceComponent property indicates if this work plane is based on a referenced component or not. This property returns Nothing in the case where it is not based on a referenced component. |
| [Shared](../WorkPlaneProxy/WorkPlaneProxy_Shared.md) | Gets and sets whether the work plane is shared or not. |
| [Type](../WorkPlaneProxy/WorkPlaneProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../WorkPlaneProxy/WorkPlaneProxy_Visible.md) | Specifies the visibility of the work plane. |

## Version

Introduced in version 5
