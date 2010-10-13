#coding:utf-8

from types import SVGElement
from tiny12attributes import property_names, media_group_names

empty_list = []

tiny12_elements = {
    'a': SVGElement('a',
    attributes=[u'about', u'class', u'content', u'datatype', u'externalResourcesRequired', u'focusHighlight', u'focusable', u'id', u'nav-down', u'nav-down-left', u'nav-down-right', u'nav-left', u'nav-next', u'nav-prev', u'nav-right', u'nav-up', u'nav-up-left', u'nav-up-right', u'property', u'rel', u'requiredExtensions', u'requiredFeatures', u'requiredFonts', u'requiredFormats', u'resource', u'rev', u'role', u'systemLanguage', u'target', u'transform', u'typeof', u'xlink:actuate', u'xlink:arcrole', u'xlink:href', u'xlink:role', u'xlink:show', u'xlink:title', u'xlink:type', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=property_names,
    children=['likeparent', 'defs', 'text', 'g', 'textArea', 'svg']),

    'animate': SVGElement('animate',
    attributes=[u'about', u'accumulate', u'additive', u'attributeName', u'attributeType', u'begin', u'by', u'calcMode', u'class', u'content', u'datatype', u'dur', u'end', u'fill', u'from', u'id', u'keySplines', u'keyTimes', u'max', u'min', u'property', u'rel', u'repeatCount', u'repeatDur', u'requiredExtensions', u'requiredFeatures', u'requiredFonts', u'requiredFormats', u'resource', u'restart', u'rev', u'role', u'systemLanguage', u'to', u'typeof', u'values', u'xlink:actuate', u'xlink:arcrole', u'xlink:href', u'xlink:role', u'xlink:show', u'xlink:title', u'xlink:type', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=empty_list,
    children=[u'desc', u'handler', u'metadata', u'switch', u'title']),

    'animateColor': SVGElement('animateColor',
    attributes=[u'about', u'accumulate', u'additive', u'attributeName', u'attributeType', u'begin', u'by', u'calcMode', u'class', u'content', u'datatype', u'dur', u'end', u'fill', u'from', u'id', u'keySplines', u'keyTimes', u'max', u'min', u'property', u'rel', u'repeatCount', u'repeatDur', u'requiredExtensions', u'requiredFeatures', u'requiredFonts', u'requiredFormats', u'resource', u'restart', u'rev', u'role', u'systemLanguage', u'to', u'typeof', u'values', u'xlink:actuate', u'xlink:arcrole', u'xlink:href', u'xlink:role', u'xlink:show', u'xlink:title', u'xlink:type', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=empty_list,
    children=[u'desc', u'handler', u'metadata', u'switch', u'title']),

    'animateMotion': SVGElement('animateMotion',
    attributes=[u'about', u'accumulate', u'additive', u'begin', u'by', u'calcMode', u'class', u'content', u'datatype', u'dur', u'end', u'fill', u'from', u'id', u'keyPoints', u'keySplines', u'keyTimes', u'max', u'min', u'origin', u'path', u'property', u'rel', u'repeatCount', u'repeatDur', u'requiredExtensions', u'requiredFeatures', u'requiredFonts', u'requiredFormats', u'resource', u'restart', u'rev', u'role', u'rotate', u'systemLanguage', u'to', u'typeof', u'values', u'xlink:actuate', u'xlink:arcrole', u'xlink:href', u'xlink:role', u'xlink:show', u'xlink:title', u'xlink:type', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=empty_list,
    children=[u'desc', u'handler', u'metadata', u'mpath', u'switch', u'title']),

    'animateTransform': SVGElement('animateTransform',
    attributes=[u'about', u'accumulate', u'additive', u'attributeName', u'attributeType', u'begin', u'by', u'calcMode', u'class', u'content', u'datatype', u'dur', u'end', u'fill', u'from', u'id', u'keySplines', u'keyTimes', u'max', u'min', u'property', u'rel', u'repeatCount', u'repeatDur', u'requiredExtensions', u'requiredFeatures', u'requiredFonts', u'requiredFormats', u'resource', u'restart', u'rev', u'role', u'systemLanguage', u'to', u'type', u'typeof', u'values', u'xlink:actuate', u'xlink:arcrole', u'xlink:href', u'xlink:role', u'xlink:show', u'xlink:title', u'xlink:type', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=empty_list,
    children=[u'desc', u'handler', u'metadata', u'switch', u'title']),

    'animation': SVGElement('animation',
    attributes=[u'about', u'begin', u'class', u'content', u'datatype', u'dur', u'end', u'externalResourcesRequired', u'fill', u'focusHighlight', u'focusable', u'height', u'id', u'initialVisibility', u'max', u'min', u'nav-down', u'nav-down-left', u'nav-down-right', u'nav-left', u'nav-next', u'nav-prev', u'nav-right', u'nav-up', u'nav-up-left', u'nav-up-right', u'preserveAspectRatio', u'property', u'rel', u'repeatCount', u'repeatDur', u'requiredExtensions', u'requiredFeatures', u'requiredFonts', u'requiredFormats', u'resource', u'restart', u'rev', u'role', u'syncBehavior', u'syncMaster', u'syncTolerance', u'systemLanguage', u'transform', u'typeof', u'width', u'x', u'xlink:actuate', u'xlink:arcrole', u'xlink:href', u'xlink:role', u'xlink:show', u'xlink:title', u'xlink:type', u'xml:base', u'xml:id', u'xml:lang', u'xml:space', u'y'],
    properties=media_group_names,
    children=[u'animate', u'animateColor', u'animateMotion', u'animateTransform', u'desc', u'discard', u'handler', u'metadata', u'set', u'switch', u'title']),

    'audio': SVGElement('audio',
    attributes=[u'about', u'begin', u'class', u'content', u'datatype', u'dur', u'end', u'externalResourcesRequired', u'fill', u'id', u'max', u'min', u'property', u'rel', u'repeatCount', u'repeatDur', u'requiredExtensions', u'requiredFeatures', u'requiredFonts', u'requiredFormats', u'resource', u'restart', u'rev', u'role', u'syncBehavior', u'syncMaster', u'syncTolerance', u'systemLanguage', u'type', u'typeof', u'xlink:actuate', u'xlink:arcrole', u'xlink:href', u'xlink:role', u'xlink:show', u'xlink:title', u'xlink:type', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=media_group_names,
    children=[u'animate', u'animateColor', u'animateMotion', u'animateTransform', u'desc', u'discard', u'handler', u'metadata', u'set', u'switch', u'title']),

    'circle': SVGElement('circle',
    attributes=[u'about', u'class', u'content', u'cx', u'cy', u'datatype', u'focusHighlight', u'focusable', u'id', u'nav-down', u'nav-down-left', u'nav-down-right', u'nav-left', u'nav-next', u'nav-prev', u'nav-right', u'nav-up', u'nav-up-left', u'nav-up-right', u'property', u'r', u'rel', u'requiredExtensions', u'requiredFeatures', u'requiredFonts', u'requiredFormats', u'resource', u'rev', u'role', u'systemLanguage', u'transform', u'typeof', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=property_names,
    children=[u'animate', u'animateColor', u'animateMotion', u'animateTransform', u'desc', u'discard', u'handler', u'metadata', u'set', u'switch', u'title']),

    'defs': SVGElement('defs',
    attributes=[u'about', u'class', u'content', u'datatype', u'id', u'property', u'rel', u'resource', u'rev', u'role', u'typeof', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=property_names,
    children=[u'a', u'animate', u'animateColor', u'animateMotion', u'animateTransform', u'animation', u'audio', u'circle', u'defs', u'desc', u'discard', u'ellipse', u'font', u'font-face', u'foreignObject', u'g', u'handler', u'image', u'line', u'linearGradient', u'listener', u'metadata', u'path', u'polygon', u'polyline', u'prefetch', u'radialGradient', u'rect', u'script', u'set', u'solidColor', u'switch', u'text', u'textArea', u'title', u'use', u'video']),

    'desc': SVGElement('desc',
    attributes=[u'about', u'class', u'content', u'datatype', u'id', u'property', u'rel', u'requiredExtensions', u'requiredFeatures', u'requiredFonts', u'requiredFormats', u'resource', u'rev', u'role', u'systemLanguage', u'typeof', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=media_group_names,
    children=empty_list),

    'discard': SVGElement('discard',
    attributes=[u'about', u'begin', u'class', u'content', u'datatype', u'id', u'property', u'rel', u'requiredExtensions', u'requiredFeatures', u'requiredFonts', u'requiredFormats', u'resource', u'rev', u'role', u'systemLanguage', u'typeof', u'xlink:actuate', u'xlink:arcrole', u'xlink:href', u'xlink:role', u'xlink:show', u'xlink:title', u'xlink:type', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=empty_list,
    children=[u'desc', u'handler', u'metadata', u'switch', u'title']),

    'ellipse': SVGElement('ellipse',
    attributes=[u'about', u'class', u'content', u'cx', u'cy', u'datatype', u'focusHighlight', u'focusable', u'id', u'nav-down', u'nav-down-left', u'nav-down-right', u'nav-left', u'nav-next', u'nav-prev', u'nav-right', u'nav-up', u'nav-up-left', u'nav-up-right', u'property', u'rel', u'requiredExtensions', u'requiredFeatures', u'requiredFonts', u'requiredFormats', u'resource', u'rev', u'role', u'rx', u'ry', u'systemLanguage', u'transform', u'typeof', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=property_names,
    children=[u'animate', u'animateColor', u'animateMotion', u'animateTransform', u'desc', u'discard', u'handler', u'metadata', u'set', u'switch', u'title']),

    'font': SVGElement('font',
    attributes=[u'about', u'class', u'content', u'datatype', u'externalResourcesRequired', u'horiz-adv-x', u'horiz-origin-x', u'id', u'property', u'rel', u'resource', u'rev', u'role', u'typeof', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=empty_list,
    children=[u'desc', u'font-face', u'glyph', u'hkern', u'metadata', u'missing-glyph', u'switch', u'title']),

    'font-face': SVGElement('font-face',
    attributes=[u'about', u'accent-height', u'alphabetic', u'ascent', u'bbox', u'cap-height', u'class', u'content', u'datatype', u'descent', u'externalResourcesRequired', u'font-family', u'font-stretch', u'font-style', u'font-variant', u'font-weight', u'hanging', u'id', u'ideographic', u'mathematical', u'overline-position', u'overline-thickness', u'panose-1', u'property', u'rel', u'resource', u'rev', u'role', u'slope', u'stemh', u'stemv', u'strikethrough-position', u'strikethrough-thickness', u'typeof', u'underline-position', u'underline-thickness', u'unicode-range', u'units-per-em', u'widths', u'x-height', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=empty_list,
    children=[u'desc', u'font-face-src', u'metadata', u'switch', u'title']),

    'font-face-src': SVGElement('font-face-src',
    attributes=[u'about', u'class', u'content', u'datatype', u'id', u'property', u'rel', u'resource', u'rev', u'role', u'typeof', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=empty_list,
    children=[u'desc', u'font-face-uri', u'metadata', u'switch', u'title']),

    'font-face-uri': SVGElement('font-face-uri',
    attributes=[u'about', u'class', u'content', u'datatype', u'externalResourcesRequired', u'id', u'property', u'rel', u'resource', u'rev', u'role', u'typeof', u'xlink:actuate', u'xlink:arcrole', u'xlink:href', u'xlink:role', u'xlink:show', u'xlink:title', u'xlink:type', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=empty_list,
    children=[u'desc', u'metadata', u'switch', u'title']),

    'foreignObject': SVGElement('foreignObject',
    attributes=[u'about', u'class', u'content', u'datatype', u'externalResourcesRequired', u'focusHighlight', u'focusable', u'height', u'id', u'nav-down', u'nav-down-left', u'nav-down-right', u'nav-left', u'nav-next', u'nav-prev', u'nav-right', u'nav-up', u'nav-up-left', u'nav-up-right', u'property', u'rel', u'requiredExtensions', u'requiredFeatures', u'requiredFonts', u'requiredFormats', u'resource', u'rev', u'role', u'systemLanguage', u'transform', u'typeof', u'width', u'x', u'xlink:actuate', u'xlink:arcrole', u'xlink:href', u'xlink:role', u'xlink:show', u'xlink:title', u'xlink:type', u'xml:base', u'xml:id', u'xml:lang', u'xml:space', u'y'],
    properties=property_names,
    children=[u'desc', u'metadata', u'svg', u'switch', u'title']),

    'g': SVGElement('g',
    attributes=[u'about', u'class', u'content', u'datatype', u'externalResourcesRequired', u'focusHighlight', u'focusable', u'id', u'nav-down', u'nav-down-left', u'nav-down-right', u'nav-left', u'nav-next', u'nav-prev', u'nav-right', u'nav-up', u'nav-up-left', u'nav-up-right', u'property', u'rel', u'requiredExtensions', u'requiredFeatures', u'requiredFonts', u'requiredFormats', u'resource', u'rev', u'role', u'systemLanguage', u'transform', u'typeof', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=property_names,
    children=[u'a', u'animate', u'animateColor', u'animateMotion', u'animateTransform', u'animation', u'audio', u'circle', u'defs', u'desc', u'discard', u'ellipse', u'font', u'font-face', u'foreignObject', u'g', u'handler', u'image', u'line', u'linearGradient', u'listener', u'metadata', u'path', u'polygon', u'polyline', u'prefetch', u'radialGradient', u'rect', u'script', u'set', u'solidColor', u'switch', u'text', u'textArea', u'title', u'use', u'video']),

    'glyph': SVGElement('glyph',
    attributes=[u'about', u'arabic-form', u'class', u'content', u'd', u'datatype', u'glyph-name', u'horiz-adv-x', u'id', u'lang', u'property', u'rel', u'resource', u'rev', u'role', u'typeof', u'unicode', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=empty_list,
    children=[u'desc', u'metadata', u'switch', u'title']),

    'handler': SVGElement('handler',
    attributes=[u'about', u'class', u'content', u'datatype', u'ev:event', u'externalResourcesRequired', u'id', u'property', u'rel', u'resource', u'rev', u'role', u'type', u'typeof', u'xlink:actuate', u'xlink:arcrole', u'xlink:href', u'xlink:role', u'xlink:show', u'xlink:title', u'xlink:type', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=empty_list,
    children=[u'desc', u'metadata', u'switch', u'title']),

    'hkern': SVGElement('hkern',
    attributes=[u'about', u'class', u'content', u'datatype', u'g1', u'g2', u'id', u'k', u'property', u'rel', u'resource', u'rev', u'role', u'typeof', u'u1', u'u2', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=empty_list,
    children=[u'desc', u'metadata', u'switch', u'title']),

    'image': SVGElement('image',
    attributes=[u'about', u'class', u'content', u'datatype', u'externalResourcesRequired', u'focusHighlight', u'focusable', u'height', u'id', u'nav-down', u'nav-down-left', u'nav-down-right', u'nav-left', u'nav-next', u'nav-prev', u'nav-right', u'nav-up', u'nav-up-left', u'nav-up-right', u'opacity', u'preserveAspectRatio', u'property', u'rel', u'requiredExtensions', u'requiredFeatures', u'requiredFonts', u'requiredFormats', u'resource', u'rev', u'role', u'systemLanguage', u'transform', u'type', u'typeof', u'width', u'x', u'xlink:actuate', u'xlink:arcrole', u'xlink:href', u'xlink:role', u'xlink:show', u'xlink:title', u'xlink:type', u'xml:base', u'xml:id', u'xml:lang', u'xml:space', u'y'],
    properties=media_group_names,
    children=[u'animate', u'animateColor', u'animateMotion', u'animateTransform', u'desc', u'discard', u'handler', u'metadata', u'set', u'switch', u'title']),

    'line': SVGElement('line',
    attributes=[u'about', u'class', u'content', u'datatype', u'focusHighlight', u'focusable', u'id', u'nav-down', u'nav-down-left', u'nav-down-right', u'nav-left', u'nav-next', u'nav-prev', u'nav-right', u'nav-up', u'nav-up-left', u'nav-up-right', u'property', u'rel', u'requiredExtensions', u'requiredFeatures', u'requiredFonts', u'requiredFormats', u'resource', u'rev', u'role', u'systemLanguage', u'transform', u'typeof', u'x1', u'x2', u'xml:base', u'xml:id', u'xml:lang', u'xml:space', u'y1', u'y2'],
    properties=property_names,
    children=[u'animate', u'animateColor', u'animateMotion', u'animateTransform', u'desc', u'discard', u'handler', u'metadata', u'set', u'switch', u'title']),

    'linearGradient': SVGElement('linearGradient',
    attributes=[u'about', u'class', u'content', u'datatype', u'gradientUnits', u'id', u'property', u'rel', u'resource', u'rev', u'role', u'typeof', u'x1', u'x2', u'xml:base', u'xml:id', u'xml:lang', u'xml:space', u'y1', u'y2'],
    properties=property_names,
    children=[u'animate', u'animateColor', u'animateMotion', u'animateTransform', u'desc', u'discard', u'metadata', u'set', u'stop', u'switch', u'title']),

    'listener': SVGElement('listener',
    attributes=[u'about', u'class', u'content', u'datatype', u'defaultAction', u'event', u'handler', u'id', u'observer', u'phase', u'propagate', u'property', u'rel', u'resource', u'rev', u'role', u'target', u'typeof', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=empty_list,
    children=empty_list),

    'metadata': SVGElement('metadata',
    attributes=[u'about', u'class', u'content', u'datatype', u'id', u'property', u'rel', u'requiredExtensions', u'requiredFeatures', u'requiredFonts', u'requiredFormats', u'resource', u'rev', u'role', u'systemLanguage', u'typeof', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=media_group_names,
    children=empty_list),

    'missing-glyph': SVGElement('missing-glyph',
    attributes=[u'about', u'class', u'content', u'd', u'datatype', u'horiz-adv-x', u'id', u'property', u'rel', u'resource', u'rev', u'role', u'typeof', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=empty_list,
    children=[u'desc', u'metadata', u'switch', u'title']),

    'mpath': SVGElement('mpath',
    attributes=[u'about', u'class', u'content', u'datatype', u'id', u'property', u'rel', u'resource', u'rev', u'role', u'typeof', u'xlink:actuate', u'xlink:arcrole', u'xlink:href', u'xlink:role', u'xlink:show', u'xlink:title', u'xlink:type', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=empty_list,
    children=[u'desc', u'metadata', u'switch', u'title']),

    'path': SVGElement('path',
    attributes=[u'about', u'class', u'content', u'd', u'datatype', u'focusHighlight', u'focusable', u'id', u'nav-down', u'nav-down-left', u'nav-down-right', u'nav-left', u'nav-next', u'nav-prev', u'nav-right', u'nav-up', u'nav-up-left', u'nav-up-right', u'pathLength', u'property', u'rel', u'requiredExtensions', u'requiredFeatures', u'requiredFonts', u'requiredFormats', u'resource', u'rev', u'role', u'systemLanguage', u'transform', u'typeof', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=property_names,
    children=[u'animate', u'animateColor', u'animateMotion', u'animateTransform', u'desc', u'discard', u'handler', u'metadata', u'set', u'switch', u'title']),

    'polygon': SVGElement('polygon',
    attributes=[u'about', u'class', u'content', u'datatype', u'focusHighlight', u'focusable', u'id', u'nav-down', u'nav-down-left', u'nav-down-right', u'nav-left', u'nav-next', u'nav-prev', u'nav-right', u'nav-up', u'nav-up-left', u'nav-up-right', u'points', u'property', u'rel', u'requiredExtensions', u'requiredFeatures', u'requiredFonts', u'requiredFormats', u'resource', u'rev', u'role', u'systemLanguage', u'transform', u'typeof', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=property_names,
    children=[u'animate', u'animateColor', u'animateMotion', u'animateTransform', u'desc', u'discard', u'handler', u'metadata', u'set', u'switch', u'title']),

    'polyline': SVGElement('polyline',
    attributes=[u'about', u'class', u'content', u'datatype', u'focusHighlight', u'focusable', u'id', u'nav-down', u'nav-down-left', u'nav-down-right', u'nav-left', u'nav-next', u'nav-prev', u'nav-right', u'nav-up', u'nav-up-left', u'nav-up-right', u'points', u'property', u'rel', u'requiredExtensions', u'requiredFeatures', u'requiredFonts', u'requiredFormats', u'resource', u'rev', u'role', u'systemLanguage', u'transform', u'typeof', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=property_names,
    children=[u'animate', u'animateColor', u'animateMotion', u'animateTransform', u'desc', u'discard', u'handler', u'metadata', u'set', u'switch', u'title']),

    'prefetch': SVGElement('prefetch',
    attributes=[u'about', u'bandwidth', u'class', u'content', u'datatype', u'id', u'mediaCharacterEncoding', u'mediaContentEncodings', u'mediaSize', u'mediaTime', u'property', u'rel', u'resource', u'rev', u'role', u'typeof', u'xlink:actuate', u'xlink:arcrole', u'xlink:href', u'xlink:role', u'xlink:show', u'xlink:title', u'xlink:type', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=empty_list,
    children=[u'desc', u'metadata', u'switch', u'title']),

    'radialGradient': SVGElement('radialGradient',
    attributes=[u'about', u'class', u'content', u'cx', u'cy', u'datatype', u'gradientUnits', u'id', u'property', u'r', u'rel', u'resource', u'rev', u'role', u'typeof', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=property_names,
    children=[u'animate', u'animateColor', u'animateMotion', u'animateTransform', u'desc', u'discard', u'metadata', u'set', u'stop', u'switch', u'title']),

    'rect': SVGElement('rect',
    attributes=[u'about', u'class', u'content', u'datatype', u'focusHighlight', u'focusable', u'height', u'id', u'nav-down', u'nav-down-left', u'nav-down-right', u'nav-left', u'nav-next', u'nav-prev', u'nav-right', u'nav-up', u'nav-up-left', u'nav-up-right', u'property', u'rel', u'requiredExtensions', u'requiredFeatures', u'requiredFonts', u'requiredFormats', u'resource', u'rev', u'role', u'rx', u'ry', u'systemLanguage', u'transform', u'typeof', u'width', u'x', u'xml:base', u'xml:id', u'xml:lang', u'xml:space', u'y'],
    properties=property_names,
    children=[u'animate', u'animateColor', u'animateMotion', u'animateTransform', u'desc', u'discard', u'handler', u'metadata', u'set', u'switch', u'title']),

    'script': SVGElement('script',
    attributes=[u'about', u'class', u'content', u'datatype', u'externalResourcesRequired', u'id', u'property', u'rel', u'resource', u'rev', u'role', u'type', u'typeof', u'xlink:actuate', u'xlink:arcrole', u'xlink:href', u'xlink:role', u'xlink:show', u'xlink:title', u'xlink:type', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=empty_list,
    children=[u'desc', u'metadata', u'switch', u'title']),

    'set': SVGElement('set',
    attributes=[u'about', u'attributeName', u'attributeType', u'begin', u'class', u'content', u'datatype', u'dur', u'end', u'fill', u'id', u'max', u'min', u'property', u'rel', u'repeatCount', u'repeatDur', u'requiredExtensions', u'requiredFeatures', u'requiredFonts', u'requiredFormats', u'resource', u'restart', u'rev', u'role', u'systemLanguage', u'to', u'typeof', u'xlink:actuate', u'xlink:arcrole', u'xlink:href', u'xlink:role', u'xlink:show', u'xlink:title', u'xlink:type', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=empty_list,
    children=[u'desc', u'handler', u'metadata', u'switch', u'title']),

    'solidColor': SVGElement('solidColor',
    attributes=[u'about', u'class', u'content', u'datatype', u'id', u'property', u'rel', u'resource', u'rev', u'role', u'typeof', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=property_names,
    children=[u'animate', u'animateColor', u'animateMotion', u'animateTransform', u'desc', u'discard', u'handler', u'metadata', u'set', u'switch', u'title']),

    'stop': SVGElement('stop',
    attributes=[u'about', u'class', u'content', u'datatype', u'id', u'offset', u'property', u'rel', u'resource', u'rev', u'role', u'typeof', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=property_names,
    children=[u'animate', u'animateColor', u'animateMotion', u'animateTransform', u'desc', u'discard', u'metadata', u'set', u'switch', u'title']),

    'svg': SVGElement('svg',
    attributes=[u'about', u'baseProfile', u'class', u'content', u'contentScriptType', u'datatype', u'externalResourcesRequired', u'focusHighlight', u'focusable', u'height', u'id', u'nav-down', u'nav-down-left', u'nav-down-right', u'nav-left', u'nav-next', u'nav-prev', u'nav-right', u'nav-up', u'nav-up-left', u'nav-up-right', u'playbackOrder', u'preserveAspectRatio', u'property', u'rel', u'resource', u'rev', u'role', u'snapshotTime', u'syncBehaviorDefault', u'syncToleranceDefault', u'timelineBegin', u'typeof', u'version', u'viewBox', u'width', u'xml:base', u'xml:id', u'xml:lang', u'xml:space', u'xmlns', u'xmlns:xlink', u'xmlns:ev', u'zoomAndPan'],
    properties=property_names,
    children=[u'a', u'animate', u'animateColor', u'animateMotion', u'animateTransform', u'animation', u'audio', u'circle', u'defs', u'desc', u'discard', u'ellipse', u'font', u'font-face', u'foreignObject', u'g', u'handler', u'image', u'line', u'linearGradient', u'listener', u'metadata', u'path', u'polygon', u'polyline', u'prefetch', u'radialGradient', u'rect', u'script', u'set', u'solidColor', u'switch', u'text', u'textArea', u'title', u'use', u'video']),

    'switch': SVGElement('switch',
    attributes=[u'about', u'class', u'content', u'datatype', u'externalResourcesRequired', u'focusHighlight', u'focusable', u'id', u'nav-down', u'nav-down-left', u'nav-down-right', u'nav-left', u'nav-next', u'nav-prev', u'nav-right', u'nav-up', u'nav-up-left', u'nav-up-right', u'property', u'rel', u'requiredExtensions', u'requiredFeatures', u'requiredFonts', u'requiredFormats', u'resource', u'rev', u'role', u'systemLanguage', u'transform', u'typeof', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=property_names,
    children=['likeparent', 'set', 'textArea', 'text', 'image', 'missing-glyph', 'font-face', 'video', 'path', 'animate', 'font', 'ellipse', 'glyph', 'use', 'font-face-src', 'polygon', 'script', 'handler', 'circle', 'radialGradient', 'prefetch', 'defs', 'mpath', 'stop', 'animateMotion', 'animateColor', 'discard', 'solidColor', 'hkern', 'line', 'animation', 'rect', 'g', 'svg', 'animateTransform', 'linearGradient', 'font-face-uri', 'foreignObject', 'polyline', 'audio']),

    'tbreak': SVGElement('tbreak',
    attributes=[u'about', u'class', u'content', u'datatype', u'id', u'property', u'rel', u'requiredExtensions', u'requiredFeatures', u'requiredFonts', u'requiredFormats', u'resource', u'rev', u'role', u'systemLanguage', u'typeof', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=empty_list,
    children=empty_list),

    'text': SVGElement('text',
    attributes=[u'about', u'class', u'content', u'datatype', u'editable', u'focusHighlight', u'focusable', u'id', u'nav-down', u'nav-down-left', u'nav-down-right', u'nav-left', u'nav-next', u'nav-prev', u'nav-right', u'nav-up', u'nav-up-left', u'nav-up-right', u'property', u'rel', u'requiredExtensions', u'requiredFeatures', u'requiredFonts', u'requiredFormats', u'resource', u'rev', u'role', u'rotate', u'systemLanguage', u'transform', u'typeof', u'x', u'xml:base', u'xml:id', u'xml:lang', u'xml:space', u'y'],
    properties=property_names,
    children=[u'a', u'animate', u'animateColor', u'animateMotion', u'animateTransform', u'desc', u'discard', u'handler', u'metadata', u'set', u'switch', u'title', u'tspan']),

    'textArea': SVGElement('textArea',
    attributes=[u'about', u'class', u'content', u'datatype', u'editable', u'focusHighlight', u'focusable', u'height', u'id', u'nav-down', u'nav-down-left', u'nav-down-right', u'nav-left', u'nav-next', u'nav-prev', u'nav-right', u'nav-up', u'nav-up-left', u'nav-up-right', u'property', u'rel', u'requiredExtensions', u'requiredFeatures', u'requiredFonts', u'requiredFormats', u'resource', u'rev', u'role', u'systemLanguage', u'transform', u'typeof', u'width', u'x', u'xml:base', u'xml:id', u'xml:lang', u'xml:space', u'y'],
    properties=property_names,
    children=[u'a', u'animate', u'animateColor', u'animateMotion', u'animateTransform', u'desc', u'discard', u'handler', u'metadata', u'set', u'switch', u'tbreak', u'title', u'tspan']),

    'title': SVGElement('title',
    attributes=[u'about', u'class', u'content', u'datatype', u'id', u'property', u'rel', u'requiredExtensions', u'requiredFeatures', u'requiredFonts', u'requiredFormats', u'resource', u'rev', u'role', u'systemLanguage', u'typeof', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=media_group_names,
    children=empty_list),

    'tspan': SVGElement('tspan',
    attributes=[u'about', u'class', u'content', u'datatype', u'focusHighlight', u'focusable', u'id', u'nav-down', u'nav-down-left', u'nav-down-right', u'nav-left', u'nav-next', u'nav-prev', u'nav-right', u'nav-up', u'nav-up-left', u'nav-up-right', u'property', u'rel', u'requiredExtensions', u'requiredFeatures', u'requiredFonts', u'requiredFormats', u'resource', u'rev', u'role', u'systemLanguage', u'typeof', u'xml:base', u'xml:id', u'xml:lang', u'xml:space'],
    properties=property_names,
    children=['likeparent', 'text', 'textArea']),

    'use': SVGElement('use',
    attributes=[u'about', u'class', u'content', u'datatype', u'externalResourcesRequired', u'focusHighlight', u'focusable', u'id', u'nav-down', u'nav-down-left', u'nav-down-right', u'nav-left', u'nav-next', u'nav-prev', u'nav-right', u'nav-up', u'nav-up-left', u'nav-up-right', u'property', u'rel', u'requiredExtensions', u'requiredFeatures', u'requiredFonts', u'requiredFormats', u'resource', u'rev', u'role', u'systemLanguage', u'transform', u'typeof', u'x', u'xlink:actuate', u'xlink:arcrole', u'xlink:href', u'xlink:role', u'xlink:show', u'xlink:title', u'xlink:type', u'xml:base', u'xml:id', u'xml:lang', u'xml:space', u'y'],
    properties=property_names,
    children=[u'animate', u'animateColor', u'animateMotion', u'animateTransform', u'desc', u'discard', u'handler', u'metadata', u'set', u'switch', u'title']),

    'video': SVGElement('video',
    attributes=[u'about', u'begin', u'class', u'content', u'datatype', u'dur', u'end', u'externalResourcesRequired', u'fill', u'focusHighlight', u'focusable', u'height', u'id', u'initialVisibility', u'max', u'min', u'nav-down', u'nav-down-left', u'nav-down-right', u'nav-left', u'nav-next', u'nav-prev', u'nav-right', u'nav-up', u'nav-up-left', u'nav-up-right', u'overlay', u'preserveAspectRatio', u'property', u'rel', u'repeatCount', u'repeatDur', u'requiredExtensions', u'requiredFeatures', u'requiredFonts', u'requiredFormats', u'resource', u'restart', u'rev', u'role', u'syncBehavior', u'syncMaster', u'syncTolerance', u'systemLanguage', u'transform', u'transformBehavior', u'type', u'typeof', u'width', u'x', u'xlink:actuate', u'xlink:arcrole', u'xlink:href', u'xlink:role', u'xlink:show', u'xlink:title', u'xlink:type', u'xml:base', u'xml:id', u'xml:lang', u'xml:space', u'y'],
    properties=media_group_names,
    children=[u'animate', u'animateColor', u'animateMotion', u'animateTransform', u'desc', u'discard', u'handler', u'metadata', u'set', u'switch', u'title']),
}
