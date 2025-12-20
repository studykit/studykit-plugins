# Autodesk Inventor 2026 API Object Model

This document summarizes the complete object model hierarchy of the Inventor 2026 API.

## Legend

- **Collection Objects**: `Objects` (plural) - Object collections
- **Standard Objects**: `Object` (singular) - Standard objects
- **Base Class Objects**: `[x]` - Base classes
- **Derived Objects**: `(x)` - Derived classes
- Color coding:
  - 🔴 User Interface Related Objects
  - 🟢 Part Document Related Objects
  - 🔵 Assembly Document Related Objects
  - 🟡 Drawing Document Related Objects
  - 🟠 Presentation Document Related Objects

---

## Application (Top-level Object)

```
Application
├── ApplicationAddIn
├── ApplicationAddIns
├── ApplicationEvents
├── Camera
├── CameraEvents
├── CheckPoint / CheckPointsEnumerator
├── ColorScheme / ColorSchemes
├── Documents
├── DocumentEvents
├── FileVersion / FileVersions
├── HighlightSet
├── InventorVBAProject / InventorVBAProjects
├── PrintManager
├── Property / PropertySet / PropertySets
├── ReferenceKeyManager
├── Transaction / TransactionManager / TransactionsEnumerator
├── TransactionEvents
├── UnitsOfMeasure
├── View / Views
└── SoftwareVersion
```

---

## Document Types

### Document [a] - Base Class

```
Document [a]
├── PartDocument (a)
├── AssemblyDocument (a)
├── DrawingDocument (a)
└── PresentationDocument (a)
```

---

## Part Document Objects

### PartDocument Structure

```
PartDocument (a)
├── PartEvents
├── PartComponentDefinition [n]
│   ├── Features → PartFeatures [bb]
│   ├── Sketches → PlanarSketches
│   ├── Sketches3D
│   ├── WorkPlanes / WorkAxes / WorkPoints
│   ├── Parameters
│   ├── SurfaceBodies
│   ├── iMateDefinitions
│   ├── Materials
│   └── MassProperties
├── SheetMetalComponentDefinition (n)
│   ├── SheetMetalFeatures (bb)
│   ├── FlatPattern (n)
│   └── SheetMetalStyles
└── DataIO
```

### Part Features [bb]

```
PartFeatures [bb]
├── ExtrudeFeature (c) / ExtrudeFeatures
├── RevolveFeature (c) / RevolveFeatures
├── SweepFeature (c) / SweepFeatures
├── LoftFeature (c) / LoftFeatures
├── HoleFeature (c) / HoleFeatures
├── FilletFeature (c) / FilletFeatures
├── ChamferFeature (c) / ChamferFeatures
├── ShellFeature (c) / ShellFeatures
├── RibFeature (c) / RibFeatures
├── CoilFeature (c) / CoilFeatures
├── ThreadFeature (c) / ThreadFeatures
├── MirrorFeature (c) / MirrorFeatures
├── CircularPatternFeature (c) / CircularPatternFeatures
├── RectangularPatternFeature (c) / RectangularPatternFeatures
├── SplitFeature (c) / SplitFeatures
├── ThickenFeature (c) / ThickenFeatures
├── EmbossFeature (c) / EmbossFeatures
├── DecalFeature (c) / DecalFeatures
├── BoundaryPatchFeature (c) / BoundaryPatchFeatures
├── RuledSurfaceFeature (c) / RuledSurfaceFeatures
├── KnitFeature (c) / KnitFeatures
├── SculptFeature (c) / SculptFeatures
├── TrimFeature (c) / TrimFeatures
├── ExtendFeature (c) / ExtendFeatures
├── FaceDraftFeature (c) / FaceDraftFeatures
├── MoveFaceFeature (c) / MoveFaceFeatures
├── ReplaceFaceFeature (c) / ReplaceFaceFeatures
├── DeleteFaceFeature (c) / DeleteFaceFeatures
├── DirectEditFeature / DirectEditFeatures
├── CombineFeature / CombineFeatures
├── iFeature (c) / iFeatures
├── ClientFeature (c) / ClientFeatures
├── NonParametricBaseFeature (c) / NonParametricBaseFeatures
├── ReferenceFeature (c) / ReferenceFeatures
├── AliasFreeformFeature (c) / AliasFreeformFeatures
├── FreeformFeature / FreeformFeatures
├── MeshFeature / MeshFeatureSets
├── UnwrapFeature (c) / UnwrapFeatures
├── SimplifyFeature (c) / SimplifyFeatures
├── MarkFeature (c) / MarkFeatures
└── FinishFeature / FinishFeatures
```

### Sheet Metal Features

```
SheetMetalFeatures (bb)
├── FaceFeature (c) / FaceFeatures
├── FlangeFeature (c) / FlangeFeatures
├── ContourFlangeFeature (c) / ContourFlangeFeatures
├── LoftedFlangeFeature (c) / LoftedFlangeFeatures
├── HemFeature (c) / HemFeatures
├── FoldFeature (c) / FoldFeatures
├── BendFeature (c) / BendFeatures
├── CutFeature (c) / CutFeatures
├── CornerFeature (c) / CornerFeatures
├── CornerChamferFeature (c) / CornerChamferFeatures
├── CornerRoundFeature (c) / CornerRoundFeatures
├── ContourRollFeature (c) / ContourRollFeatures
├── PunchToolFeature (c) / PunchToolFeatures
├── RipFeature (c) / RipFeatures
├── UnfoldFeature (c) / UnfoldFeatures
├── RefoldFeature (c) / RefoldFeatures
├── CosmeticBendFeature (c) / CosmeticBendFeatures
└── BendPartFeature (c) / BendPartFeatures
```

### Feature Extent Types [e]

```
PartFeatureExtent [e]
├── DistanceExtent (e)
├── AngleExtent (e)
├── ThroughAllExtent (e)
├── ToNextExtent (e)
├── ToExtent (e)
├── FromToExtent (e)
├── FullSweepExtent (e)
├── DistanceFromFaceExtent (e)
├── CutAcrossBendsExtent (e)
├── PitchAndHeightCoilExtent (e)
├── PitchAndRevolutionCoilExtent (e)
├── RevolutionAndHeightCoilExtent (e)
├── SpiralCoilExtent (e)
├── CenteredWidthExtent (e)
├── EdgeWidthExtent (e)
├── FromToWidthExtent (e)
├── OffsetWidthExtent (e)
├── WidthOffsetWidthExtent (e)
├── DistanceHeightExtent (e)
├── LegacyDistanceHeightExtent (e)
└── ToHeightExtent (e)
```

---

## Assembly Document Objects

### AssemblyDocument Structure

```
AssemblyDocument (a)
├── AssemblyEvents
├── AssemblyOptions
├── AssemblyComponentDefinition [m]
│   ├── ComponentOccurrence / ComponentOccurrences
│   ├── AssemblyConstraints
│   ├── AssemblyJoints
│   ├── BOM / BOMViews
│   ├── OccurrencePatterns
│   ├── iMateResults
│   ├── Parameters
│   ├── WorkPlanes / WorkAxes / WorkPoints
│   └── MassProperties
└── DataIO
```

### Assembly Constraints [l]

```
AssemblyConstraint [l]
├── MateConstraint (l)
├── AngleConstraint (l)
├── TangentConstraint (l)
├── InsertConstraint (l)
├── FlushConstraint (l)
├── RotateRotateConstraint (l)
├── RotateTranslateConstraint (l)
├── TranslateTranslateConstraint (l)
├── TransitionalConstraint (l)
├── AssemblySymmetryConstraint (l)
├── CustomConstraint
└── LayoutConstraint
```

### Assembly Joints

```
AssemblyJoint
├── AssemblyJointDefinition
└── AssemblyJoints
```

### Occurrence Patterns [k]

```
OccurrencePattern [k]
├── RectangularOccurrencePattern (k)
├── CircularOccurrencePattern (k)
└── FeatureBasedOccurrencePattern (k)
```

### iMate Definitions [o]

```
iMateDefinition [o]
├── MateiMateDefinition (o)
├── AngleiMateDefinition (o)
├── TangentiMateDefinition (o)
├── InsertiMateDefinition (o)
├── FlushiMateDefinition (o)
├── RotateRotateiMateDefinition (o)
├── RotateTranslateiMateDefinition (o)
└── CompositeiMateDefinition (o)
```

### BOM (Bill of Materials)

```
BOM
├── BOMView / BOMViews
├── BOMRow / BOMRowsEnumerator
└── BOMQuantity
```

---

## Drawing Document Objects

### DrawingDocument Structure

```
DrawingDocument (a)
├── DrawingEvents
├── DrawingOptions
├── DrawingSettings
├── DrawingPrintManager
├── DrawingStylesManager
├── Sheet / Sheets
│   ├── DrawingView / DrawingViews
│   ├── DrawingDimension / DrawingDimensions
│   ├── DrawingNote / DrawingNotes
│   ├── Balloon / Balloons
│   ├── PartsList / PartsLists
│   ├── CustomTable / CustomTables
│   ├── HoleTable / HoleTables
│   ├── RevisionTable / RevisionTables
│   ├── TitleBlock
│   ├── Border
│   └── SketchedSymbol / SketchedSymbols
└── DataIO
```

### Drawing Views [v]

```
DrawingView [v]
├── SectionDrawingView (v)
├── DetailDrawingView (v)
├── DrawingViewLabel
├── DrawingCurve / DrawingCurvesEnumerator
└── DrawingCurveSegment / DrawingCurveSegments
```

### Drawing Dimensions [ff]

```
DrawingDimension [ff]
├── GeneralDimension (ff) [u]
│   ├── LinearGeneralDimension (u)
│   ├── AngularGeneralDimension (u)
│   ├── RadiusGeneralDimension (u)
│   └── DiameterGeneralDimension (u)
├── OrdinateDimension (ff)
└── BaselineDimensionSet / ChainDimensionSet
```

### Drawing Notes [aa]

```
DrawingNote [aa]
├── GeneralNote (aa)
├── LeaderNote (aa) [jj]
├── BendNote (jj)
├── ChamferNote (jj)
├── HoleThreadNote (jj)
└── PunchNote (jj)
```

### Tables

```
PartsList / PartsLists
├── PartsListRow / PartsListRows
├── PartsListColumn / PartsListColumns
└── PartsListCell

CustomTable / CustomTables
├── Row / Rows
├── Column / Columns
└── Cell

HoleTable / HoleTables
RevisionTable / RevisionTables
DrawingBOM / DrawingBOMs
```

---

## 2D Sketch Objects

### Sketch [p] Structure

```
Sketch [p] (PlanarSketch / DrawingSketch)
├── SketchEntities
│   ├── SketchPoint (r)
│   ├── SketchLine (r)
│   ├── SketchArc (r)
│   ├── SketchCircle (r)
│   ├── SketchEllipse (r)
│   ├── SketchEllipticalArc (r)
│   ├── SketchSpline (r)
│   ├── SketchFixedSpline (r)
│   ├── SketchOffsetSpline (r)
│   ├── SketchControlPointSpline (r)
│   └── SketchEquationCurve (r)
├── GeometricConstraints
├── DimensionConstraints
├── Profile / Profiles
├── SketchImage / SketchImages
├── TextBox / TextBoxes
├── SketchBlock / SketchBlocks
├── SketchBlockDefinition / SketchBlockDefinitions
└── SketchFillRegion / SketchFillRegions
```

### Geometric Constraints [q]

```
GeometricConstraint [q]
├── CoincidentConstraint (q)
├── CollinearConstraint (q)
├── ConcentricConstraint (q)
├── ParallelConstraint (q)
├── PerpendicularConstraint (q)
├── HorizontalConstraint (q)
├── VerticalConstraint (q)
├── TangentSketchConstraint (q)
├── SmoothConstraint (q)
├── SymmetryConstraint (q)
├── EqualLengthConstraint (q)
├── EqualRadiusConstraint (q)
├── MidpointConstraint (q)
├── OffsetConstraint (q)
├── GroundConstraint (q)
├── HorizontalAlignConstraint (q)
├── VerticalAlignConstraint (q)
├── PatternConstraint (q)
└── SplineFitPointConstraint (q)
```

### Dimension Constraints [s]

```
DimensionConstraint [s]
├── TwoPointDistanceDimConstraint (s)
├── TwoLineAngleDimConstraint (s)
├── ThreePointAngleDimConstraint (s)
├── RadiusDimConstraint (s)
├── DiameterDimConstraint (s)
├── OffsetDimConstraint (s)
├── EllipseRadiusDimConstraint (s)
├── TangentDistanceDimConstraint (s)
└── ArcLengthDimConstraint (s)
```

---

## 3D Sketch Objects

### Sketch3D Structure

```
Sketch3D
├── SketchEntities3D
│   ├── SketchPoint3D (j)
│   ├── SketchLine3D (j)
│   ├── SketchArc3D (j)
│   ├── SketchCircle3D (j)
│   ├── SketchEllipse3D (j)
│   ├── SketchEllipticalArc3D (j)
│   ├── SketchSpline3D (j)
│   ├── SketchFixedSpline3D (j)
│   ├── SketchControlPointSpline3D (j)
│   ├── SketchEquationCurve3D (j)
│   ├── OnFaceCurve (j)
│   ├── HelicalCurve
│   ├── SilhouetteCurve
│   ├── IntersectionCurve
│   └── ProjectToSurfaceCurve
├── GeometricConstraints3D
├── DimensionConstraints3D
└── Profile3D / Profiles3D
```

### 3D Geometric Constraints [h]

```
GeometricConstraint3D [h]
├── CoincidentConstraint3D (h)
├── CollinearConstraint3D (h)
├── ParallelConstraint3D (h)
├── PerpendicularConstraint3D (h)
├── TangentConstraint3D (h)
├── SmoothConstraint3D (h)
├── GroundConstraint3D (h)
├── BendConstraint (h)
├── HelicalConstraint3D (h)
├── SplineFitPointsConstraint3D (h)
├── EqualConstraint3D (h)
├── OnFaceConstraint3D (h)
├── CustomConstraint3D (h)
├── ParallelToXAxisConstraint3D (h)
├── ParallelToYAxisConstraint3D (h)
├── ParallelToZAxisConstraint3D (h)
├── ParallelToXYPlaneConstraint3D (h)
├── ParallelToXZPlaneConstraint3D (h)
└── ParallelToYZPlaneConstraint3D (h)
```

### 3D Dimension Constraints [y]

```
DimensionConstraint3D [y]
├── TwoPointDistanceDimConstraint3D (y)
├── TwoLineAngleDimConstraint3D (y)
├── LineLengthDimConstraint3D (y)
├── PointAndPlaneDistanceDimConstraint3D (y)
├── RadiusDimConstraint3D (y)
└── SplineLengthDimConstraint3D (y)
```

---

## Work Features

```
WorkPlane / WorkPlanes
├── FixedWorkPlaneDef
├── PlaneAndOffsetWorkPlaneDef
├── PlaneAndPointWorkPlaneDef
├── ThreePointsWorkPlaneDef
├── TwoLinesWorkPlaneDef
├── TwoPlanesWorkPlaneDef
├── LineAndTangentWorkPlaneDef
├── LinePlaneAndAngleWorkPlaneDef
├── NormalToCurveWorkPlaneDef
├── PlaneAndTangentWorkPlaneDef
├── PointAndTangentWorkPlaneDef
└── TorusMidPlaneWorkPlaneDef

WorkAxis / WorkAxes
├── FixedWorkAxisDef
├── LineWorkAxisDef
├── TwoPointsWorkAxisDef
├── TwoPlanesWorkAxisDef
├── LineAndPlaneWorkAxisDef
├── LineAndPointWorkAxisDef
├── NormalToSurfaceWorkAxisDef
├── RevolvedFaceWorkAxisDef
└── AnalyticEdgeWorkAxisDef

WorkPoint / WorkPoints
├── FixedWorkPointDef
├── PointWorkPointDef
├── MidPointWorkPointDef
├── TwoLinesWorkPointDef
├── ThreePlanesWorkPointDef
├── CurveAndEntityWorkPointDef
├── NonLinearEdgeWorkPointDef
├── CentroidWorkPointDef
├── SphereCenterPointWorkPointDef
└── TorusCenterPointWorkPointDef
```

---

## B-Rep (Boundary Representation)

```
SurfaceBody / SurfaceBodies
├── FaceShell / FaceShells
│   ├── Face / Faces
│   │   ├── EdgeLoop / EdgeLoops
│   │   │   ├── Edge / Edges
│   │   │   └── EdgeUse / EdgeUses
│   │   └── Vertex / Vertices
│   └── SurfaceEvaluator
├── Wire / Wires
├── CurveEvaluator
└── Curve2dEvaluator
```

---

## Transient Geometry & Objects

### Geometry Objects

```
Arc2d / Arc3d
BSplineCurve2d / BSplineCurve
BSplineCurve2dDefinition / BSplineCurveDefinition
BSplineSurface
Box / Box2d
Circle2d / Circle
Cone
Cylinder
Ellipse / EllipseFull / EllipseFull2d
EllipticalArc / EllipticalArc2d
EllipticalCone
EllipticalCylinder
Line / Line2d
LineSegment / LineSegment2d
Plane
Polyline2d / Polyline3d
Sphere
Torus
```

### Math Objects

```
Point / Point2d
Vector / Vector2d
UnitVector / UnitVector2d
Matrix / Matrix2d
OrientedBox
```

### Utility Objects

```
Camera
Color
DataMedium
EdgeCollection
FaceCollection
FileMetadata
NameValueMap
ObjectCollection
ObjectCollectionByVariant
ObjectsEnumeratorByVariant
TranslationContext
```

---

## User Interface Objects

### CommandManager & UI

```
CommandManager
├── ControlDefinitions
│   ├── ButtonDefinition (b)
│   ├── ComboBoxDefinition (b)
│   └── MacroControlDefinition (b)
├── CommandBar / CommandBars
├── CommandCategories / CommandCategory
├── DisabledCommandList
├── Ribbon / Ribbons
│   ├── RibbonTab / RibbonTabs
│   └── RibbonPanel / RibbonPanels
└── CommandControl / CommandControls

UserInterfaceManager
├── Environment / Environments
├── EnvironmentManager
├── DockableWindow / DockableWindows
├── MiniToolbar
│   ├── MiniToolbarButton (hh)
│   ├── MiniToolbarCheckBox (hh)
│   ├── MiniToolbarComboBox (hh)
│   ├── MiniToolbarDropdown (hh)
│   ├── MiniToolbarSlider (hh)
│   ├── MiniToolbarTextBox (hh)
│   └── MiniToolbarValueEditor (hh)
├── RadialMarkingMenu / RadialMarkingMenus
├── BalloonTip / BalloonTips
├── ProgressBar
└── ProgressiveToolTip
```

### Browser

```
BrowserPane / BrowserPanes
├── BrowserNode / BrowserNodesEnumerator
├── BrowserFolder / BrowserFoldersEnumerator
└── BrowserNodeDefinition [ee]
    ├── ClientBrowserNodeDefinition (ee)
    └── NativeBrowserNodeDefinition (ee)
```

### Events

```
InteractionEvents
├── MouseEvents
├── KeyboardEvents
├── SelectEvents
└── TriadEvents

UserInputEvents
UserInterfaceEvents
DockableWindowsEvents
HelpEvents
FileUIEvents
BrowserPanesEvents
SearchBoxEvents
ManipulatorEvents
```

---

## Client Graphics

```
ClientGraphicsCollection
├── ClientGraphics
│   └── GraphicsNode
│       ├── GraphicsPrimitive [gg]
│       │   ├── PointGraphics (gg)
│       │   ├── LineGraphics (gg)
│       │   ├── LineStripGraphics (gg)
│       │   ├── CurveGraphics (gg)
│       │   ├── TriangleGraphics
│       │   ├── TriangleFanGraphics
│       │   ├── TriangleStripGraphics
│       │   └── TextGraphics
│       └── SurfaceGraphics
│           ├── SurfaceGraphicsFace / FaceList
│           ├── SurfaceGraphicsEdge / EdgeList
│           └── SurfaceGraphicsVertex / VertexList
└── GraphicsDataSetsCollection
    └── GraphicsDataSet [dd]
        ├── GraphicsColorSet (dd)
        ├── GraphicsCoordinateSet (dd)
        ├── GraphicsIndexSet (dd)
        ├── GraphicsNormalSet (dd)
        ├── GraphicsTextureCoordinateSet (dd)
        └── GraphicsImageSet (dd)
```

---

## Assets (Materials & Appearances)

```
AssetLibrary / AssetLibraries
├── Asset
│   ├── AssetCategory / AssetCategories
│   ├── AssetTexture
│   └── AssetValue [mm]
│       ├── BooleanAssetValue (mm)
│       ├── IntegerAssetValue (mm)
│       ├── FloatAssetValue (mm)
│       ├── StringAssetValue (mm)
│       ├── ChoiceAssetValue (mm)
│       ├── ColorAssetValue (mm)
│       ├── FilenameAssetValue (mm)
│       ├── ReferenceAssetValue (mm)
│       └── TextureAssetValue (mm)
└── ProjectAssetLibrary / ProjectAssetLibraries
```

---

## Parameters

```
Parameters
├── Parameter [i]
│   ├── ModelParameter (i)
│   ├── UserParameter (i)
│   ├── ReferenceParameter (i)
│   ├── TableParameter (i)
│   └── DerivedParameter
├── ParameterTable / ParameterTables
├── DerivedParameterTable / DerivedParameterTables
├── CustomParameterGroup / CustomParameterGroups
├── Tolerance
├── ExpressionLimits
├── ExpressionList
└── CustomPropertyFormat
```

---

## Attributes

```
AttributeManager
├── AttributeSet / AttributeSets
│   └── Attribute
├── AttributesEnumerator
└── AttributeSetsEnumerator
```

---

## Model Annotations

```
ModelAnnotations
├── ModelDimension [jj]
│   ├── LinearModelDimension (jj)
│   ├── AngularModelDimension (jj)
│   ├── RadiusModelDimension (jj)
│   └── DiameterModelDimension (jj)
├── ModelLeaderNote
├── ModelHoleThreadNote (jj)
├── ModelFeatureControlFrame
├── ModelDatumIdentifier
├── ModelSurfaceTextureSymbol
├── ModelGeneralNote
├── ModelCompositeAnnotation
├── ModelWeldingSymbol
├── ModelDatum / ModelDatumTarget
└── AnnotationPlane / AnnotationPlanes
```

---

## Styles [z]

```
Style [z] / Styles
├── DimensionStyle (z)
├── TextStyle (z)
├── Layer (z)
├── LightingStyle (z)
├── DrawingStandardStyle (z)
├── ObjectDefaultsStyle (z)
├── BalloonStyle (z)
├── CentermarkStyle (z)
├── FeatureControlFrameStyle (z)
├── HoleTableStyle (z)
├── LeaderStyle (z)
├── PartsListStyle (z)
├── RevisionTableStyle (z)
├── SurfaceTextureStyle (z)
├── TableStyle (z)
├── SheetMetalStyle (z)
├── UnfoldMethod (z)
├── EdgeSymbolStyle (z)
└── WeldSymbolStyle (z)
```

---

## Model States

```
ModelStates
├── ModelState
├── ModelStateTable
│   ├── ModelStateTableRow / ModelStateTableRows
│   ├── ModelStateTableColumn / ModelStateTableColumns
│   └── ModelStateTableCell
└── ModelStateEvents
```

---

## Representations

```
RepresentationsManager
├── DesignViewRepresentation / DesignViewRepresentations
├── PositionalRepresentation / PositionalRepresentations
└── RepresentationEvents
```

---

## Derived Components

```
DerivedPartComponent / DerivedPartComponents
├── DerivedPartDefinition [cc]
│   ├── DerivedPartTransformDef (cc)
│   ├── DerivedPartUniformScaleDef (cc)
│   └── DerivedPartCoordinateSystemDef (cc)
└── DerivedPartEntities / DerivedPartEntity

DerivedAssemblyComponent / DerivedAssemblyComponents
├── DerivedAssemblyDefinition
└── DerivedAssemblyOccurrence / DerivedAssemblyOccurrences

ShrinkwrapComponent / ShrinkwrapComponents
└── ShrinkwrapDefinition

DerivedFuturePartComponent / DerivedFuturePartComponents
└── DerivedFuturePartDefinition

DerivedFutureAssemblyComponent / DerivedFutureAssemblyComponents
└── DerivedFutureAssemblyDefinition
```

---

## Imported Components

```
ImportedComponent / ImportedComponents
├── ImportedComponentDefinition
├── ImportedGenericComponentDefinition
├── ImportedDWGComponent
├── ImportedRVTComponent
├── ImportedDataExchangeComponent
└── ImportedModelEntity / ImportedModelEntities
```

---

## iFeature & iPart/iAssembly

### iFeature

```
iFeature (c) / iFeatures
├── iFeatureDefinition
├── iFeatureInput [t]
│   ├── iFeatureEntityInput (t)
│   ├── iFeatureParameterInput (t)
│   ├── iFeatureSketchPlaneInput (t)
│   ├── iFeatureVectorInput (t)
│   └── iFeatureWorkPlaneInput (t)
├── iFeatureTable
└── iFeatureTemplateDescriptor / iFeatureTemplateDescriptors
```

### iPart

```
iPartFactory
├── iPartMember
├── iPartTableRow / iPartTableRows
├── iPartTableColumn / iPartTableColumns
└── iPartTableCell
```

### iAssembly

```
iAssemblyFactory
├── iAssemblyMember
├── iAssemblyTableRow / iAssemblyTableRows
├── iAssemblyTableColumn / iAssemblyTableColumns
└── iAssemblyTableCell
```

---

## Content Center

```
ContentCenter
├── ContentFamily / ContentFamiliesEnumerator
├── ContentTreeViewNode / ContentTreeViewNodesEnumerator
├── ContentTableRow / ContentTableRows
├── ContentTableColumn / ContentTableColumns
├── ContentTableCell
└── ContentCenterOptions
```

---

## BIM Exchange

```
BIMComponent
├── BIMComponentDescription
├── BIMConnector / BIMConnectors
│   ├── BIMCableTrayConnector / BIMCableTrayConnectorDefinition
│   ├── BIMConduitConnector / BIMConduitConnectorDefinition
│   ├── BIMDuctConnector / BIMDuctConnectorDefinition
│   ├── BIMElectricalConnector / BIMElectricalConnectorDefinition
│   └── BIMPipeConnector / BIMPipeConnectorDefinition
└── BIMConnectorLink / BIMConnectorLinks
```

---

## Dynamic Simulation

```
SimulationManager
├── DynamicSimulation / DynamicSimulations
├── DSSettings
├── DSJoint / DSJoints / DSJointDefinition
├── DSLoad / DSLoads / DSLoadDefinition
├── DSResult / DSResults
├── DSDegreeOfFreedom / DSDegreesOfFreedom
└── DSValue / DSValueGraph
```

---

## Apprentice Server

```
ApprenticeServer
├── ApprenticeServerDocument / ApprenticeServerDocuments
├── ApprenticeServerDrawingDocument
├── ApprenticeServerComponent
├── ApprenticePrintManager
├── ApprenticeDrawingPrintManager
├── ClientView / ClientViews
├── FileSaveAs
├── FileManager / File / FilesEnumerator
├── DesignProjectManager / DesignProjects
├── SoftwareVersion
├── TransientGeometry
└── TransientObjects
```

---

## Presentation Document Objects

```
PresentationDocument (a)
├── PresentationScene / PresentationScenes
├── PresentationSnapshotView / PresentationSnapshotViews
├── PresentationTrail / PresentationTrails
│   └── PresentationTrailSegment / PresentationTrailSegments
├── PresentationComponent / PresentationComponentsEnumerator
├── PresentationBody / PresentationBodiesEnumerator
├── PresentationFace / PresentationFacesEnumerator
├── PresentationEdge / PresentationEdgesEnumerator
├── PresentationVertex / PresentationVerticesEnumerator
└── PresentationMeshFeature / PresentationMeshFeatureSets
```

---

## Point Clouds

```
PointClouds
├── PointCloud
├── PointCloudScan / PointCloudScans
├── PointCloudRegion / PointCloudRegions
└── PointCloudCrop / PointCloudCrops
```

---

## Weldment

```
WeldmentComponentDefinition (m)
├── Weld / Welds
├── WeldBead / WeldBeads
├── CosmeticWeld / CosmeticWelds
├── CosmeticWeldDefinition
└── WeldsComponentDefinition
```

---

## File Management

```
FileManager
├── File / FilesEnumerator
├── FileDescriptor / FileDescriptorsEnumerator
├── DocumentDescriptor / DocumentDescriptorsEnumerator
├── FileAccessEvents
├── FileManagerEvents
└── FileOptions

FileDialog
├── FileDialogEvents
└── FactoryTableDialog

DesignProjectManager
├── DesignProject / DesignProjects
├── ProjectPath / ProjectPaths
└── LibraryFolder / LibraryFolders
```

---

## Data I/O

```
DataIO
├── TranslatorAddIn
├── DataMedium
└── TranslationContext
```

---

## Mesh Features

```
MeshFeature
├── MeshFeatureSet / MeshFeatureSets
├── MeshFeatureEntity [nn]
│   ├── MeshFace (nn)
│   ├── MeshEdge (nn)
│   └── MeshVertex (nn)
└── MeshFeatureEntitiesEnumerator
```

---

## Revit Export

```
RevitExport / RevitExports
└── RevitExportDefinition
```

---

## Additional Objects

### Change Management

```
ChangeManager
├── ChangeProcessor
├── ChangeDefinition / ChangeDefinitions
└── Transaction / TransactionManager
```

### Error Handling

```
ErrorManager
└── MessageSection
```

### Options & Settings

```
Application Options:
├── GeneralOptions
├── FileOptions
├── DisplayOptions
├── HardwareOptions
├── AssemblyOptions
├── PartOptions
├── DrawingOptions
├── SketchOptions
├── Sketch3DOptions
├── NotebookOptions
├── ContentCenterOptions
├── FactoryOptions
├── iFeatureOptions
├── SaveOptions
├── GripSnapOptions
├── PromptsOptions
├── HeadsUpDisplayOptions
├── PresentationOptions
├── SpellCheckOptions
└── SelectionPreferences
```

### Miscellaneous

```
Machining / Preparations
LanguageTools
MeasureTools
ThreadTableQuery
ThemeManager / Theme
WebBrowserDialog / WebBrowserDialogs
SearchBox
VisibleOccurrenceFinder
```

---

## Version Information

- **Document Date**: Dec 12, 2024
- **Inventor Version**: 2026
- **Source**: InventorObjectModel.pdf
