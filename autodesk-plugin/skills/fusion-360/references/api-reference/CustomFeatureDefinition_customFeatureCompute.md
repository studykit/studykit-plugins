# CustomFeatureDefinition.customFeatureCompute Event![](../images/TestTubeLarge.png)

Parent Object: [CustomFeatureDefinition](CustomFeatureDefinition.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CustomFeatureDefinition.h>

## Description

The customFeatureCompute event fires when Fusion is computing the timeline and reaches the custom feature. The event is fired if any of the dependencies of the custom feature have changed. You can modify the results of your custom feature based on the dependencies.

## Syntax

* [Python Using fusion360utils](#PythonUsingFusion360Utils)
* [Python](#Python)
* [C++](#C++)

*-------- Import ---------* |

*-------- Global variables ---------* ```` ``` # Global variable used to maintain a reference to all event handlers. handlers = [] ``` ```` *-------- Connect the handler to the event. ---------* ```` ``` # "customFeatureDefinition_var" is a variable referencing a CustomFeatureDefinition object. # "MyCustomFeatureComputeHandler" is the name of the class that handles the event. onCustomFeatureCompute = MyCustomFeatureComputeHandler() customFeatureDefinition_var.customFeatureCompute.add(onCustomFeatureCompute) handlers.append(onCustomFeatureCompute) ``` ```` *-------- Event handler class definition ---------* ```` ``` # Event handler for the customFeatureCompute event. class MyCustomFeatureComputeHandler(adsk.fusion.CustomFeatureEventHandler):     def __init__(self):         super().__init__()     def notify(self, args: adsk.fusion.CustomFeatureEventArgs):         # Code to react to the event.         app.log('In MyCustomFeatureComputeHandler event handler.') ``` ```` |

*--------- Required include files. ---------* ```` ``` #include <Fusion/Features/CustomFeatureDefinition.h> #include <Fusion/Features/CustomFeatureEvent.h> #include <Fusion/Features/CustomFeatureEventHandler.h> #include <Fusion/Features/CustomFeatureEventArgs.h> ``` ````  *--------- Event handler class definition and global declaration. --------- ```` ``` // Event handler for the customFeatureCompute event. ``` ````* class MyCustomFeatureComputeEventHandler : public adsk::fusion::CustomFeatureEventHandler { public:  void notify(const Ptr<CustomFeatureEventArgs>& eventArgs) override  {  // Code to react to the event.  ui->messageBox("In MyCustomFeatureComputeEventHandler event handler.");  } } \_customFeatureCompute;  *--------- Connect the handler to the event. ---------* ```` ``` // "customFeatureDefinition_var" is a variable referencing a CustomFeatureDefinition object. // Connect the handler function to the event. Ptr<CustomFeatureEvent> customFeatureComputeEvent = customFeatureDefinition_var->customFeatureCompute(); if (!customFeatureComputeEvent)     return;  bool isOk = customFeatureComputeEvent->add(&_customFeatureCompute); if (!isOk)     return; ``` ```` |

## Property Value

This is an event property that returns a [CustomFeatureEvent](CustomFeatureEvent.htm).

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |